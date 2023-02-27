import requests
import os
import json
from kafka import KafkaProducer
from urllib3.exceptions import ProtocolError
import os
import datetime
import socket

class Filtered_stream(object): 

    def __init__(self, index, query, api):
        self.query = query 
        self.bearer_token = api 
        self.index =  index
        
        """self.conn = conn
        self.addr = addr"""

        self.tweetIDfile = 'tweetID/tweetID.txt'

        

    def main(self):
        print(self.query, self.bearer_token)
        while True:
            try:
                self.rules = self.get_rules()
                self.delete = self.delete_all_rules(self.rules)
                self.set = self.set_rules(self.delete)
                self.get_stream(self.set)
            except Exception as es:
                print(self.index,"retry",es)
                continue

    def bearer_oauth(self,r):
        """
        Method required by bearer token authentication.
        """
        r.headers["Authorization"] = "Bearer {}".format(self.bearer_token)
        r.headers["User-Agent"] = "v2FilteredStreamPython"
        return r


    def get_rules(self):
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream/rules", auth=self.bearer_oauth
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
            )
        print(self.index, json.dumps(response.json()))
        return response.json()


    def delete_all_rules(self, rules):
        if rules is None or "data" not in rules:
            return None

        ids = list(map(lambda rule: rule["id"], rules["data"]))
        payload = {"delete": {"ids": ids}}
        response = requests.post(
            "https://api.twitter.com/2/tweets/search/stream/rules",
            auth=self.bearer_oauth,
            json=payload
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot delete rules (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        print(self.index, json.dumps(response.json()))


    def set_rules(self, delete):
        # You can adjust the rules if needed
        sample_rules = [
            {"value": self.query}
        ]
        payload = {"add": sample_rules}
        response = requests.post(
            "https://api.twitter.com/2/tweets/search/stream/rules",
            auth=self.bearer_oauth,
            json=payload,
        )
        if response.status_code != 201:
            raise Exception(
                "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
            )
        print(self.index, json.dumps(response.json()))


    def get_stream(self, set):
        self.producer = KafkaProducer(acks=0, compression_type='gzip', api_version=(0, 10, 1), bootstrap_servers=[''])
        self.count = 1
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=referenced_tweets.id", auth=self.bearer_oauth, stream=True,
        )
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Cannot get stream (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        for response_line in response.iter_lines():
            if response_line:
                json_response = json.loads(response_line)
                try:
                    json_response['topic'] = "topic"
                    json_response['start_timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    tweet_json = json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False)
                    #print(self.index, self.query, self.count )
                    result_print = "{0:<10}|query={1:<20}|count={2:<10}|".format(
                        self.index,
                        self.query,
                        self.count)
                    print(result_print)
                    
                    ## TO KAFKA
                    self.producer.send("tweet", tweet_json.encode('utf-8'))
                    self.producer.flush()

                    ## TO tcp Spark
                    #self.conn.send((json.dumps(json_response)+"\n").encode('utf-8'))

                    
                    self.count = self.count  + 1 
                    with open(self.tweetIDfile, 'a') as f:
                        f.write(str(json_response['data']['id']+","))
                        #f.write(str(json_response['start_timestamp'])+","+str(json_response['data']['id'])+"\n")
                except Exception as es:
                    print(es, self.query)
                    continue
