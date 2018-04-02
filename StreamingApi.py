import config
import json
import requests
from requests_oauthlib import OAuth1
from pymongo import MongoClient

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

client = MongoClient('localhost', 27017)

auth = OAuth1(CK, CS, AT, ATS)

url = "https://stream.twitter.com/1.1/statuses/sample.json?language=ja"

res = requests.post(url, auth=auth, stream = True)

collection = client.test_collection
count = 0
if res.status_code == 200:
    print("connect succeed")
    for line in res.iter_lines():
        tweet = {}
        stream = line.decode("utf-8")
        find = json.loads(stream)
        print(find['user']['name'] + '::'+find['text'])
        print('*******************************************')
        tweet['id'] = find['id']
        tweet['text'] = find['text']
        tweet['created_at'] = find['created_at']
        tweet['user'] = {'screen_name' : tweet['user']['screen_name']}
        collection.insert(tweet)
    print("正常")
else:
    print("Error: %d" %res.status_code)
#if __name__ == '__main__':
 #   collect(1)
