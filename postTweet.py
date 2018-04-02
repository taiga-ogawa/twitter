#!/usr/bin/env python

import json
import config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)#認証処理

url = 'https://api.twitter.com/1.1/statuses/update.json'

print("内容を入力してください")
tweet = input('>>')#キーボード入力の取得
print('************************')

params = {"status" : tweet}

res = twitter.post(url, params = params)

if res.status_code == 200:
    print("Success.")
else:
    print("Error. : %d" % res.status_code)