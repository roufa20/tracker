# Trakers Facebook and Twitter

## Requirements

Facepy python depandancy 

## Config

to configure your tracker pleas change this 2 files:

* For Facebook change this file [FACEBOOK](http://188.165.159.218/RD/trackers/blob/master/paramsFacebook.yaml) 
* For Twitter change this file [TWITTER](http://188.165.159.218/RD/trackers/blob/master/paramsTwitter.yaml) 


## Config Params

## Facebook:

* entete : is the CSV file header

* id : is the last comment id tracked

* last_update_time : is the last time this script is stopped

* status :  if you want to start tracking facebook comment and status from beginning pleas make the value of status 0, if you want it auto-incremente put it 1

* access_token : this is a facebook Access Token generated only one time by the script [FACEBOOK ACCESS TOCKEN](http://188.165.159.218/RD/trackers/blob/master/get_accet_token.py)

* lastUpdate : is the last time that the accesstocken is generated

* servers : there is 3 servers (ServerOne, ServerTwo, ServerThree) is the KAFKA servers 

## Twitter:

* entete : is the csv file Header

* keywords : twitter key for exemple if you want to track all the tweet that contain #tunisiana put this value to tunisiana

* since_id : last tweet tracked id

* access_token : tweeter access Tocken (there is 2 access tocken the script take the new one based on the lastUpdate value, this value is changed one we used, that's mean we balance between access token)

* servers : there is 3 servers (ServerOne, ServerTwo, ServerThree) is the KAFKA servers 


## CSV Files

all Facebook csv files is in facebook_data

all Twittercsv files is in twitter_data


## To chnge the Exalead Instances

Modifie the SITE value


## If you want to run this project 

./script_a_executer.sh


## CRON runing 

To run this project in cron [tutorial for Cron](https://doc.ubuntu-fr.org/cron)

## Connectors files:

* facebook_connector.py
* twitter_connector.py

## Connector + Kaka Producers files:

* facebook_producer.py
* twitter_producer.py
