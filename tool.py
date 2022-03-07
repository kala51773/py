import json
import os
from pymongo import MongoClient
class tool:
    def __init__(self):
        self.file_list = os.listdir()
        self.json_list = []

    def merge(self):
        db=self.connect()
        for file in self.file_list:
            if file.rfind("json")!=-1:
                print(file)
                f = open(file)
                content = json.loads(f.read())
                for i in content:
                    print(i)
                    if db!=None:
                        db.Spider.insert_one(i)
                    self.json_list.append(i)
        f=open('json合集.json','w')
        f.write(json.dumps(self.json_list))
    def connect(self):
        try:
            client=MongoClient('mongodb://ip:27017/')
            db=client['Spider']
            return db
        except:
            print("连接数据库时发生错误")



a =tool()
a.merge()
# a.connect()