
from pymongo import MongoClient
import StreamingApi

client = MongoClient('localhost', 27017)

db = client.mydb

tweets = StreamingApi.
