import argparse 
import requests
import json
import sys
import time
import maya
import random
import socket
import urllib.parse
import urllib.request
from pytz import timezone
import datetime
KST = timezone('Asia/Seoul')
import os
import time
from itertools import repeat
import socket
import multiprocessing
# We must import this explicitly, it is not imported by the top-level
# multiprocessing module.
import multiprocessing.pool
import time
from stem.control import Controller
from stem import Signal
<<<<<<< HEAD
import pytz
=======
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e

# 로그 생성
import logging

## import file
import AuthenticationManager
import GetCursor

## set kafka
from kafka import KafkaProducer
from pymongo import MongoClient

import configparser
config = configparser.ConfigParser()
config.read('config.ini')


class ScrapingEngine(object):
    def __init__(self, query, port, language, x_guest_token, conn, addr):
        """## Setting tweet id
        self.tweetIDfile = 'tweetID/tweetID.txt'.format(query)
        if os.path.exists(self.tweetIDfile ):
            os.remove(self.tweetIDfile )
            print("The tweetIDfile has been deleted successfully")
        else:
            print("The tweetIDfile does not exist!")
        
        os.makedirs(os.path.dirname(self.tweetIDfile), exist_ok=True)  
        self.tweetIDlogger = logging.getLogger()
        self.tweetIDlogger.setLevel(logging.WARNING)
        self.formatter = logging.Formatter('%(asctime)s - %(message)s')
        self.file_handler = logging.FileHandler(self.tweetIDfile)
        self.file_handler.setFormatter(self.formatter)
        self.tweetIDlogger.addHandler(self.file_handler)"""
        
        """## Setting logger 
        self.logfile = 'log/log_{}.txt'.format(query)
        # self.logfile = 'log/log_{}_{}.txt'.format(query,language)
        if os.path.exists(self.logfile ):
            os.remove(self.logfile )
            print("The logfile has been deleted successfully")
        else:
            print("The logfile does not exist!")
        
        os.makedirs(os.path.dirname(self.logfile), exist_ok=True)  

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.WARNING)
        self.formatter = logging.Formatter('%(asctime)s - %(message)s')
        self.file_handler = logging.FileHandler(self.logfile)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)"""

        ## Setting query
        self.query = query
        if self.query in ["Russia","Ukraine","Putin","War","#Ukraine"]:
            self.topic = "russia"
        elif self.query in ["BTS","@BTS_twt","#BTS","Jimin","RM"]:
            self.topic = "bts"
        elif self.query in ["Bitcoin","BTC","Ethereum","ETH","Cryptocurrency"]:
            self.topic = "bitcoin"
        elif self.query in ["COVID","COVID-19","WHO","coronavirus","corona"]:
            self.topic = "covid"
        
        ## Setting authorization keysets
        self.x_guest_token = x_guest_token 
        
        ## Setting init  
        self.cursor = None
        self.totalcount = 0
        self.port = port
<<<<<<< HEAD
        #self.proxies = {'http': 'socks5h://localhost:'+str(self.port-1000),} 

        ## Setting url
        self.url = "https://twitter.com/search?q={}&src=typed_query&f=live".format("until:2022-03-31 since:2022-02-01 "+self.query)
        
        ## Setting Language type
        self.accept_language = language
        self.x_twitter_client_language = language
        
        self.send_mode = config['DEFAULT']['SEND_MODE']
        if self.send_mode == "tcp":
            self.conn = conn
            self.addr = addr
        elif self.send_mode == "kafka":
            self.set_kafka()
        elif self.send_mode == "mongodb":
            #self.client = MongoClient(host="117.17.189.206:20329")
            self.username = urllib.parse.quote_plus('jbyou')
            self.password = urllib.parse.quote_plus('gkdl1533!?')
            self.client = MongoClient('mongodb://%s:%s@117.17.189.206:20329/admin?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+1.6.2' % (self.username, self.password))
            self.db = self.client['admin']
            self.collection = self.db['ftweet']
        

    def set_kafka(self):
        print("setting kafka")
        bootstrap_servers = ['117.17.189.205:9092','117.17.189.205:9093','117.17.189.205:9094']
=======
        self.proxies = {'http': 'socks5h://localhost:'+str(self.port-1000),} 

        ## Setting url
        self.url = "https://twitter.com/search?q={}&src=typed_query&f=live".format(self.query)
        
        ## Setting Language type
        self.accept_language = language
        self.x_twitter_client_language = language
        
        self.conn = conn
        self.addr = addr
        #self.tweetIDlogger = tweetIDlogger

        ## Setting send mode:
        self.set_kafka()

    def set_kafka(self):
        print("setting kafka")
        bootstrap_servers = ['']
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
        self.producer = KafkaProducer(acks=1, compression_type='gzip', api_version=(0, 10, 1), bootstrap_servers=bootstrap_servers)
    
    def set_tor(self):
        print("setting tor", self.port)
        with Controller.from_port(port = self.port) as controller:
            controller.authenticate(password="MyStr")
            controller.signal(Signal.NEWNYM)
    
    def start_scraping(self):
        request_count = 0 

        while (True):
            time.sleep(1) 

            request_count = request_count + 1

            if request_count == 100 :
                request_count = 0
<<<<<<< HEAD
                #self.set_tor()
=======
                self.set_tor()
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
                self.x_guest_token = AuthenticationManager.get_x_guest_token()

            self.headers = {
                'Accept': '*/*',
                'Accept-Language': self.accept_language,
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Referer': self.url,
                'x-guest-token': self.x_guest_token,
                'x-twitter-client-language': self.x_twitter_client_language,
                'x-twitter-active-user': 'yes',
                'x-csrf-token': '00ff4b71ba34a615506bb933894f55e1',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'Connection': 'keep-alive',
            }

            self.params = {
                'include_profile_interstitial_type': '1',
                'include_blocking': '1',
                'include_blocked_by': '1',
                'include_followed_by': '1',
                'include_want_retweets': '1',
                'include_mute_edge': '1',
                'include_can_dm': '1',
                'include_can_media_tag': '1',
                'include_ext_has_nft_avatar': '1',
                'include_ext_is_blue_verified': '1',
                'skip_status': '1',
                'cards_platform': 'Web-12',
                'include_cards': '1',
                'include_ext_alt_text': 'true',
                'include_ext_limited_action_results': 'false',
                'include_quote_count': 'true',
                'include_reply_count': '1',
                'tweet_mode': 'extended',
                'include_ext_collab_control': 'true',
                'include_entities': 'true',
                'include_user_entities': 'true',
                'include_ext_media_color': 'true',
                'include_ext_media_availability': 'true',
                'include_ext_sensitive_media_warning': 'true',
                'include_ext_trusted_friends_metadata': 'true',
                'send_error_codes': 'true',
                'simple_quoted_tweet': 'true',
<<<<<<< HEAD
                'q': "until:2022-03-31 since:2022-02-01 "+self.query,
=======
                'q': self.query,
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
                'tweet_search_mode': 'live',
                'count': '100',
                'query_source': 'typed_query',
                'pc': '1',
                'spelling_corrections': '1',
                'include_ext_edit_control': 'true',
                'cursor': self.cursor,
                'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe',
            }

            """## setting header
            self.headers = {
                    'Accept': '*/*',
                    'Accept-Language': self.accept_language,
                    'x-guest-token': self.x_guest_token,
                    'x-twitter-client-language': self.x_twitter_client_language,
                    'x-twitter-active-user': 'yes',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                    'Referer': self.url,
                    'Connection': 'keep-alive',
                    'TE': 'trailers',
            }
            
            ## setting parameters
            self.params = (
                    ('include_profile_interstitial_type', '1'),
                    ('include_blocking', '1'),
                    ('include_blocked_by', '1'),
                    ('include_followed_by', '1'),
                    ('include_want_retweets', '1'),
                    ('include_mute_edge', '1'),
                    ('include_can_dm', '1'),
                    ('include_can_media_tag', '1'),
                    ('skip_status', '1'),
                    ('cards_platform', 'Web-12'),
                    ('include_cards', '1'),
                    ('include_ext_alt_text', 'true'),
                    ('include_quote_count', 'true'),
                    ('include_reply_count', '1'),
                    ('tweet_mode', 'extended'),
                    ('include_entities', 'true'),
                    ('include_user_entities', 'true'),
                    ('include_ext_media_color', 'true'),
                    ('include_ext_media_availability', 'true'),
                    ('send_error_codes', 'true'),
                    ('simple_quoted_tweet', 'true'),
                    ('q', self.query),
                    ('tweet_search_mode', 'live'),
                    ('count', '100'),
                    ('query_source', 'typed_query'),
                    ('pc', '1'),
                    ('spelling_corrections', '1'),
                    ('ext', 'mediaStats,highlightedLabel'),
                    ('cursor', self.cursor ), ## next cursor range
            )"""
                 
            ## api requests 
            try:
                self.response = requests.get(
                        'https://twitter.com/i/api/2/search/adaptive.json', 
                        headers=self.headers,
                        params=self.params,
                        proxies=self.proxies,
                        timeout=3
                        )
                self.response_json = self.response.json()
                self.tweets = self.response_json['globalObjects']['tweets'].values()
            except Exception as ex:
                result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|requests-error={3}|".format(
                    self.port,
                    self.accept_language,
                    self.query,
                    str(ex)
                )
                #self.logger.critical(result_print)
                print(result_print)
                self.x_guest_token = AuthenticationManager.get_x_guest_token()
                #self.set_tor()
                time.sleep(5)
                continue
            else:
                self.get_tweets(self.tweets)

                ## cursor reset
                self.cursor = GetCursor.get_scroll_cursor(self.response_json)
                result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|tweet_count={3:<10}|".format(
                    self.port,
                    self.accept_language,
                    self.query,
                    str(self.totalcount)
                )
                print(result_print)
                #self.logger.critical(result_print)
            
    def get_tweets(self,tweets):  
        ## tweets to tweet
        for tweet in tweets: 
            try:                   
                self.totalcount = self.totalcount + 1
<<<<<<< HEAD
                # 'Mon Feb 13 08:40:02 +0000 2023' 
                tweet['topic'] = self.topic
                #print(tweet['topic'])
                tweet['created_at'] = maya.parse(tweet['created_at']).datetime()
                
                if tweet['created_at'] >= datetime.datetime(2022, 3, 31, tzinfo=pytz.UTC) or tweet['created_at'] <= datetime.datetime(2022, 2, 1, tzinfo=pytz.UTC):
                    print(tweet['created_at'], "2022, 2, 1 < tweet['created_at'] < 2022, 3, 31")
                    continue
                #tweet['created_at'] = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S  %Y')
                tweet['start_timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
=======
                tweet['start_timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                """result_print = "{}\n".format(str(tweet['id_str']))
                self.tweetIDlogger.critical(result_print)
                with open(self.tweetIDfile, 'a') as f:
                    f.write(str(tweet['id_str'])+"\n")"""
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
            except Exception as ex:
                result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|add_tweet_columns={3:<10}|".format(
                    self.port,
                    self.accept_language,
                    self.query,
                    str(ex))
                #self.logger.critical(result_print)
                print(result_print)
                continue
            
<<<<<<< HEAD
            if self.send_mode == "kafka":
                try:
                    ## TO KAFKA 
                    tweet_json = json.dumps(tweet, indent=4, sort_keys=True, ensure_ascii=False)
                    self.producer.send("tweet", value=tweet_json.encode('utf-8'))
                    self.producer.flush()
                except Exception as ex:
                    result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|TO KAFKA={3:<10}|".format(
                        self.port,
                        self.accept_language,
                        self.query,
                        str(ex))
                    #self.logger.critical(result_print)
                    print(result_print) 
            
            

            elif self.send_mode == "tcp":
                try:
                    ## TO tcp Spark
                    #self.conn.send((results+"\n").encode('utf-8'))
                    self.conn.send((json.dumps(tweet)+"\n").encode('utf-8'))
                except Exception as ex:
                    result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|TO Spark Engine={3:<10}|".format(
                        self.port,
                        self.accept_language,
                        self.query,
                        str(ex))
                    #self.logger.critical(result_print)
                    print(result_print)

            elif self.send_mode == "mongodb":
                try:
                    ## TO Mongodb
                    #tweet_json = json.dumps(tweet, indent=4, sort_keys=True, ensure_ascii=False)
                    self.collection.insert_one(tweet)
                except Exception as ex:
                    result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|TO Mongodb={3:<10}|".format(
                        self.port,
                        self.accept_language,
                        self.query,
                        str(ex))
                    #self.logger.critical(result_print)
                    print(result_print)
=======
            try:
                ## TO KAFKA 
                tweet_json = json.dumps(tweet, indent=4, sort_keys=True, ensure_ascii=False)
                self.producer.send("tweet", value=tweet_json.encode('utf-8'))
                self.producer.flush()
            except Exception as ex:
                result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|TO KAFKA={3:<10}|".format(
                    self.port,
                    self.accept_language,
                    self.query,
                    str(ex))
                #self.logger.critical(result_print)
                print(result_print) 
            
            try:
                ## TO tcp Spark
                #self.conn.send((results+"\n").encode('utf-8'))
                self.conn.send((json.dumps(tweet)+"\n").encode('utf-8'))
            except Exception as ex:
                result_print = "{0:<10}|lan_type={1:<10}|query={2:<20}|TO Spark Engine={3:<10}|".format(
                    self.port,
                    self.accept_language,
                    self.query,
                    str(ex))
                #self.logger.critical(result_print)
                print(result_print)
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
                
