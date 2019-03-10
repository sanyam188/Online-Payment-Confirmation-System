import xlrd
from pymongo import MongoClient
from tkinter import *

class Update(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        loc = ("../bank.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        client = MongoClient("mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/reg?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        db=client.reg
        coll=db.regs        
        unverified_docs = coll.find({'hostelv': False })
        print(unverified_docs.count())
        for ob in unverified_docs:
            du = ob['hostel']
            i=0
            for i in range(0,sheet.nrows):
                if du in sheet.cell_value(i,1):
                    aa =(sheet.cell_value(i,2))
                    if(str(ob['rollno']) in str(aa)):
                        coll.update_one({'hostel':du},{ "$set" : {'hostelv':'true'}})
                        break

        lbl = ttk.Label(self,text = "Elements in the Database are Up to date with the excel file.")
        lbl.grid()