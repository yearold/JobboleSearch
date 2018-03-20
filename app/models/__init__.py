#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pymongo
import re


class MongoSQL():

    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.client['jobbole']
        self.table = self.db['jobbole']

    def find_where(self, page):
        result = self.table.find({'title': re.compile(page, re.I)})
        return result

    def find_all(self):
        return self.table.find()