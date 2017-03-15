#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, \
    unicode_literals
from datetime import *
import logging
import os
import os.path as path
import json
from facepy import *
from langid.langid import LanguageIdentifier, model
import yaml
import io

#variables global
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
DIR = path.dirname(path.realpath(__file__))
LOG_DIR = "logs"


#facebook_origin = codecs.open("facebook_origin.json", "a", encoding='utf-8')
facebook = io.open("facebook_data/facebook_"+datetime.strftime(datetime.utcnow(),"%Y-%m-%d")+".csv", "a",encoding='utf-8-sig')
options_feed = dict()
options_comments= dict()
options_likes =dict()
with open('paramsFacebook.yaml', 'r') as file_conf:
    params= yaml.load(file_conf)


def create_logger(file, name):
    if not path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(path.join(LOG_DIR, file), encoding="utf-8")
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


#from json to csv (default separateur is '/t' tabulation)
def jsontocsv(doc,entete):
    columns=[]
    for i,column in enumerate(entete):
        if (column in doc):
            columns.append(unicode(doc[column].replace("\t"," ").replace("\r"," ").replace("\n"," ")))
        else:
            columns.append(unicode(""))
    return unicode("\t".encode("utf-8").join(columns))


#
def cleanDoc(item,type_doc,fb_page):
    doc = dict()   
    doc['id'] = item['id']
    doc['type'] = type_doc

    if 'message' in item:
        doc['message'] = item['message']
    else :
        doc['message'] =""

    doc['created_time'] =str(datetime.strptime(item["created_time"],"%Y-%m-%dT%H:%M:%S+0000")).encode("utf-8")

    if 'comments' in item and 'summary' in item['comments']:
        doc['comments_count'] = str(item['comments']['summary']['total_count'])
    else:
        doc['comments_count']="0"

    if 'shares' in item:
        doc['shares_count'] = str(item['shares']['count'])
    else :
        doc['shares_count'] = "0"
    if 'likes' in item and 'summary' in item['likes']:
        doc['likes_count'] = str(item['likes']['summary']['total_count'])
    else:
        doc['likes_count']="0"
    doc['from_id'] = item['from']['id']
    doc['from_name'] = item['from']['name']    
    try:
        language_identifier = identifier.classify(item['description'])
        item_language = language_identifier[0].upper()
        doc['language'] = item_language
    except (KeyError, TypeError):
        doc['language'] = fb_page['language']
    return doc


def send_request(graph,id,type,option,LOGGER,status,fields):
    i=0
    while (i<10):
        try:
            if (status == 0):        
                return graph.get(id + '/'+type, page=True, retry=1, fields=fields,**option)
            else:
                return graph.get(id + '/'+type, page=False, retry=1, fields=fields,**option)
        except FacepyError as exception_facepy:
            LOGGER['facebook'].error("FacepyError")
            LOGGER['facebook'].error(exception_facepy)
            if (option["limit"]>25):
                option["limit"]=option["limit"]-25
            else :
                option["limit"]=5
            i+=1
        except FacebookError as exception_facebook:
            LOGGER['facebook'].error("FacebookError")
            LOGGER['facebook'].error(exception_facebook)
            if (option["limit"]>25):
                option["limit"]=option["limit"]-25
            else :
                option["limit"]=5
            i+=1
    return dict()

#verif if grapgh api Return List or yield de list    
def verif_return_data(item,all_items):
    if ( (type(item)==dict and 'data' in item and item['data'] and len(item['data'])>0) or (type(item)==unicode and 'data'==item and len(all_items['data'])>0) ):    
            return True
    return False
    
def get_likes(graph,id,updated_time):
    LOGGER['facebook'].info("Processing " +id + "/likes at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
    all_likes =send_request(graph,id,"likes",options_likes,LOGGER,0,"fields=id,name")
    for likes in all_likes :
        if verif_return_data(likes,all_likes):
            if (type(likes)==dict):
                data_likes = likes['data']
            else:
                data_likes = all_likes['data']
            for like in data_likes:
                LOGGER['facebook'].info("Processing like " +like['id'] + " at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
                facebook.write(id+"\t"+like["id"]+"\t"+like["name"]+"\t"+updated_time+"\t"+""+"\t"+""+"\t"+"like"+"\t"+"0"+"\t"+"0"+"\t"+"0"+"\n")

def get_comments(graph,id,status_scan,updated_time,fields,fb_page,entete):
    LOGGER['facebook'].info("Processing " +id + "/comments at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
    all_comments =send_request(graph,id,"comments",options_comments,LOGGER,status_scan,fields)
    for comments in all_comments :
        if verif_return_data(comments,all_comments):    
            if (type(comments)==dict):
                data_comment = comments['data']
            else:
                data_comment = all_comments['data']
            
            for row in data_comment:
                LOGGER['facebook'].info("Processing comment " +row['id'] + " at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
                comment_post_created_time=str(datetime.strptime(row["created_time"],"%Y-%m-%dT%H:%M:%S+0000"))
                if (status_scan==0 or (status_scan== 1 and comment_post_created_time > updated_time)):
                    #get_likes(graph,row['id'],comment_post_created_time)
                    doc = cleanDoc(row,'comment',fb_page)                                     
                    facebook.write(jsontocsv(doc,entete)+'\n')                        
                else :                                    
                    LOGGER['facebook'].info("comment already fetched "+row['id']) 

def search_process(graph,fb_page,entete,fields):
    try:
        status_scan = fb_page['status']
    except (KeyError, TypeError):
        status_scan = 0    
    
    updated_time=""
    if status_scan == 1:  # existing page
        updated_time=fb_page["last_update_time"]
        #options_feed['since'.encode("UTF-8")]=fb_page["last_update_time"]
        #options_comments['since'.encode("UTF-8")]=fb_page["last_update_time"]
    LOGGER['facebook'].info("Processing " + fb_page['id'] + "/posts at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
    all_posts = send_request(graph,fb_page['id'],"posts",options_feed,LOGGER,status_scan,fields)
    LOGGER['facebook'].info("done Processing all post" + " at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
    for posts in all_posts :             
        if verif_return_data(posts,all_posts): 
            if (type(posts)==dict):
                data_feed = posts['data']
            else:
                data_feed = all_posts['data']
            for item in data_feed:
                LOGGER['facebook'].info("Processing post " + item['id'] + " at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))            
                post_created_time=str(datetime.strptime(item["created_time"],"%Y-%m-%dT%H:%M:%S+0000"))     
                if ("updated_time" in item):
                    post_updated_time=str(datetime.strptime(item["updated_time"],"%Y-%m-%dT%H:%M:%S+0000"))
                    
                    if (status_scan ==0 or updated_time <  post_updated_time):
                        LOGGER['facebook'].info("updated post to scan "+item['id'])
                        status = cleanDoc(item,'status',fb_page)
                        facebook.write(jsontocsv(status,entete)+'\n')
                        #print(options_comments)                        
                        #get_likes(graph,item['id'],post_updated_time)
                        get_comments(graph,item['id'],status_scan,updated_time,fields,fb_page,entete)

                    else:
                        LOGGER['facebook'].info("post already fetched "+item['id'])
                LOGGER['facebook'].info("finished processing post " + item['id'] + " at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))                   
                    

if __name__ == '__main__':
    LOGGER = dict()
    LOGGER['facebook'] = create_logger("facebook_"+datetime.strftime(datetime.utcnow(),"%Y-%m-%d")+".log", 'facebook')
    LOGGER['facebook'].info("Starting crawling .")

    token = params["tokens"][0]

    accessToken = token['access_token']
    
    entete=params['entete']
    #facebook.write(unicode(entete))
    #facebook.write("\n")
    projects = params['project']
    fields="fields="+params['fields']
    graph = GraphAPI(accessToken,LOGGER)
    for i,fb in enumerate(projects):
        LOGGER['facebook'].info("Processing " + fb['id']+ "at "+datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S"))
        
        options_feed["limit".encode("UTF-8")]=projects[i]["limit_posts".encode("UTF-8")]
        options_comments["limit".encode("UTF-8")] =projects[i]["limit_comments".encode("UTF-8")]
        options_likes["limit".encode("UTF-8")] =projects[i]["limit_likes".encode("UTF-8")]
        search_process(graph,fb,params['entete'].split(','),fields)   
        
        projects[i]["last_update_time".encode("UTF-8")]=datetime.strftime(datetime.utcnow(),"%Y-%m-%d %H:%M:%S").encode("UTF-8")
        LOGGER['facebook'].info("donne all processing " +projects[i]["last_update_time".encode("UTF-8")])
        projects[i]["status".encode("UTF-8")]=1
        projects[i]["limit_posts".encode("UTF-8")]=options_feed["limit".encode("UTF-8")]
        projects[i]["limit_comments".encode("UTF-8")]=options_comments["limit".encode("UTF-8")]
        with open('paramsFacebook.yaml', 'w') as file_conf:
            yaml.dump(params, file_conf, default_flow_style=False)

        # solr.optimize()
    facebook.close()