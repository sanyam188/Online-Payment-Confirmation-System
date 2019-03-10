from pymongo import MongoClient 

class db_connect():
    def __init__(self):
        cleint = MongoClient("mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        db = cleint.reg
        coll = db.regs
