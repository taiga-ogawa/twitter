#!/usr/bin/env python

from requests_oauthlib import OAuth1Session
import json
import config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)#認証処理

#タイムライン取得のURL
#home(ホーム画面)とuser(自分のツイート)
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {'count':5}
res = twitter.get(url, params = params)

if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
