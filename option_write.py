from pymongo import MongoClient
from tkinter import *

import xlwt
from xlwt import Workbook
from tkinter import filedialog
from dbconnect import db_connect
class Write(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        wb = Workbook() 
  

        sheet1 = wb.add_sheet('Sheet 1') 
        
        sheet1.write(1, 0, 'Name') 
        sheet1.write(1, 1, 'Roll Number') 
        sheet1.write(1, 2, 'DU Reference Number') 
        sheet1.write(1, 3, 'Verified') 
        client = MongoClient("mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        coll = client.reg.regs
        res = coll.find({'hostel':{"$exists":True},'name':{"$exists":True},'rollno':{"$exists":True},'hostelv':{"$exists":True}})
        co=res.count()
        for i in range(0,co):
            sheet1.write((i+2),0,res[i]['name'])
            sheet1.write((i+2),1,res[i]['rollno'])
            sheet1.write((i+2),2,res[i]['hostel'])
            sheet1.write((i+2),3,res[i]['hostelv'])

        print(coll.find({}).count())
        
        filename = filedialog.asksaveasfilename()
        wb.save(filename) 
