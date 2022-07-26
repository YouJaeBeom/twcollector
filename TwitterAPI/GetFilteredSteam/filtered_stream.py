import requests
import os
import json
from kafka import KafkaProducer
from urllib3.exceptions import ProtocolError
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGiFPQEAAAAAu7suubjKWeoDZ6WJnyn%2Bw%2BvzsTQ%3DOwureac7DLPKKfzomS4aIkZrvIMsiIseiYGM35NjLrG0DW908X"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = "Bearer {}".format(bearer_token)
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": 'bts -is:retweet'},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    producer = KafkaProducer(acks=0, compression_type='gzip', api_version=(0, 10, 1), bootstrap_servers=['117.17.189.205:9092','117.17.189.205:9093','117.17.189.205:9091'])

    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=referenced_tweets.id", auth=bearer_oauth, stream=True,
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
                refer=str(json_response['data']['referenced_tweets'][0]['type'])
                if str(refer) != "quoted":
                    producer.send("tweet_api", json.dumps(json_response).encode('utf-8'))
                    producer.flush()
                    print(json_response)
                    #print(json.dumps(json_response, sort_keys=True))
            except Exception as es:
                producer.send("tweet_api", json.dumps(json_response).encode('utf-8'))
                producer.flush()
                print(json_response)
                #print(json.dumps(json_response, sort_keys=True)) 
            


def main():
    while True:
        try:
            rules = get_rules()
            delete = delete_all_rules(rules)
            set = set_rules(delete)
            get_stream(set)
        except Exception as es:
            print("retry")
            continue


if __name__ == "__main__":
    main()
