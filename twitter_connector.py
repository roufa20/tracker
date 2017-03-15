#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, \
    unicode_literals

import json
import logging
import os
import os.path as path
import yaml
import arrow
from TwitterSearch import *
from datetime import datetime
import io
DIR = path.dirname(path.realpath(__file__))
LOG_DIR = "logs"

LOGGER = dict()

#twitter_origin = open("twitter_origin.json", "a")
twitter = io.open("twitter_data/twitter_"+datetime.strftime(datetime.now(),"%Y-%m-%d")+".csv", "a",encoding='utf-8-sig')
with open('paramsTwitter.yaml', 'r') as file_conf:
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

def get_index_token(tokens):
    date=""
    index=0;
    for i,token in enumerate(tokens):
        if (date=="" ):
            date=token["lastUpdate"]
            index=i
        elif (date>token["lastUpdate"]):
            date=token["lastUpdate"]
            index=i
    return index
def jsontocsv(doc,entete):
    columns=[]
    for i,column in enumerate(entete):
        if (column in doc):
            columns.append(unicode(doc[column].replace("\t"," ").replace("\r"," ").replace("\n"," ")))
    return unicode("\t".encode("utf-8").join(columns))
def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
    queries, tweets_seen = current_ts_instance.get_statistics()
    if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
        time.sleep(30) # sleep for 60 seconds
#@threads(5)
def search_process(ts, config,entete):
    try:
        tso = TwitterSearchOrder()
        tso.set_result_type('mixed')
        tso.set_include_entities(False) 
        main_keyword = config['keywords'].split(';')
        #main_keyword="apple;US".split(";")
        if 'requiredKeywords' in config:
            required_keywords = config['requiredKeywords'].split(',')
            if len(required_keywords) > 0:
                for key in required_keywords:
                    main_keyword.append(key)

        # pp.pprint(main_keyword)
        tso.set_keywords(main_keyword)        
        since_id = 12345
        try:
            since_id = config['since_id']
        except (KeyError, TypeError):        
            LOGGER['twitter'].info("First crawling Keyword %s." % config['keywords'])
        tso.set_since_id(since_id)
        LOGGER['twitter'].info("crawling from id "+str(since_id))
        total = 0
        new_since_id = None
        #print("searching")
        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
            '''twitter_origin.write(json.dumps(tweet))
            twitter_origin.write('\n')'''
            total+=1
            if new_since_id is None:
                new_since_id = tweet['id']
            LOGGER['twitter'].info("processing tweet  id "+ str(tweet['id']))   
            doc = dict()
            doc['id'] = str(tweet['id'])
            doc["message"] = tweet['text']
            doc["type"] = "STATUS".encode('utf-8')
            doc['created_time'] = str(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')).encode('utf-8')      
            doc['from_id'] = str(tweet['user']['id'])
            doc['from_name'] = tweet['user']['name']
            doc["favorite_count"] = str(tweet['favorite_count']).encode('utf-8')
            doc["retweet_count"] = str(tweet['retweet_count']).encode('utf-8')
            doc["language"] = tweet['lang']
            twitter.write(jsontocsv(doc,entete))
            twitter.write('\n')

        
        
        LOGGER['twitter'].info("Crawler finished: {} new items from keyword: {} ".format(total, config['keywords']))
        
        if new_since_id is None:
            return since_id    
        return new_since_id
    except TwitterSearchException as e:
            LOGGER['twitter'].error(e)
if __name__ == '__main__':

    LOGGER['twitter'] = create_logger("twitter_"+datetime.strftime(datetime.now(),"%Y-%m-%d")+".log", 'twitter')
    LOGGER['twitter'].info("Starting crawler.")

    entete=params['entete']

    #twitter.write(entete)
    #twitter.write("\n")

    index_token=get_index_token(params["tokens"])

    token = params["tokens"][index_token]
    params["tokens"][index_token]["lastUpdate"]=datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    with open('paramsTwitter.yaml', 'w') as file_conf:
            yaml.dump(params, file_conf, default_flow_style=False)
    ts = TwitterSearch(
        consumer_key=token['consumer_key'],
        consumer_secret=token['consumer_secret'],
        access_token=token['access_token'],
        access_token_secret=token['access_token_secret'],
    )
    #db.tokens.update_one(
    #    {'_id': token['_id']},
    #    {'$currentDate': {'lastUpdate': {'$type': 'date'}}}
    #)

    project = params['project']
    for i,row in enumerate(project):
        LOGGER['twitter'].info("Start Processing Project %s." % row['name'])        
        LOGGER['twitter'].info("Start Processing Keywords %s." % row['keywords'])
        params['project'][i][('since_id').encode('utf-8')]=search_process(ts, row,entete.split(","))
        with open('paramsTwitter.yaml', 'w') as file_conf:
            yaml.dump(params, file_conf, default_flow_style=False)


    #twitter_origin.close()
    twitter.close()            
    #solr.optimize()
