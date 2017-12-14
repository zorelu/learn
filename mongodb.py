#-*- coding: UTF-8 -*-
from pymongo import MongoClient
import uniout
from pprint import pprint

client = MongoClient('120.78.132.90', 7017)
db = client.b2b
db.authenticate("zorelu", "123123zz")
a=raw_input("input url:")
item = db.user.find({"code":a});
for rows in item:
    pprint (rows)
