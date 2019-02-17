from tkinter import *
from tkinter import ttk
from tkinter import *
from pymongo import MongoClient
class View(Frame):
    def __init__(self,parent,controller):

        
        Frame.__init__(self,parent)
        choice= StringVar()
        rbt1=Radiobutton(self,text='Name',variable=choice,value='1')
        rbt2=Radiobutton(self,text='Branch',variable=choice,value='2')
        rbt3=Radiobutton(self,text='Roll Number',variable=choice,value='3')
        rbt4=Radiobutton(self,text='Fees Paid',variable=choice,value='4')
        rbt5=Radiobutton(self,text='Fees Unpaid',variable=choice,value='5')      
        rbt6=Radiobutton(self,text='',variable=choice,value='6')
        
        print(choice.get())

        rbt1.grid(row=1,column=0,sticky="w")
        rbt2.grid(row=2,column=0,sticky="w")
        rbt3.grid(row=3,column=0,sticky="w")
        rbt4.grid(row=4,column=0,sticky="w")
        rbt5.grid(row=5,column=0,sticky="w")
        rbt6.grid(row=6,column=0,sticky="w")    

        print('choice',(choice.get()))
        op=StringVar()
        opp=StringVar()
        entrybtn = Entry(self,textvariable=op)
        entrybtn.grid(row=7,column=1,sticky="nsew")
        op.set("Enter Your Choice")
        
        submitbtn = Button(self,command=lambda:self.callback(choice,op),text="Submit").grid(row=8,column=1)
        
        print(opp,choice)

        self.rowconfigure( 0,weight=1)
        self.rowconfigure( 1,weight=1)
        self.rowconfigure( 2,weight=1)
        self.rowconfigure( 3,weight=1)
        self.rowconfigure( 4,weight=1)
        self.rowconfigure( 5,weight=1)
        self.rowconfigure( 6,weight=1)
        self.rowconfigure( 7,weight=1)
        self.rowconfigure( 8,weight=1)
        self.rowconfigure( 9,weight=12)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        
        
        
        
        # lbl = ttk.Label(self,text = "View Page")
        # lbl.grid()


    def callback(self,choice,op):
        rbt_choice=StringVar()
        entry_choice=StringVar()
        rbt_choice=choice.get()
        entry_choice=op.get()
        print(rbt_choice,entry_choice)
        dd = self.display_data(rbt_choice,entry_choice)

    def display_data(self,rbt_choice,entry_choice):

        client = MongoClient("mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        db=client.reg
        coll=db.regs

        if(rbt_choice == '1'):
            if(entry_choice=='Enter Your Choice'):
                print("Enter name in entry your choice column.")
            else:
                res = coll.find({'name': entry_choice})   
        elif(rbt_choice == '2'):
            if(entry_choice=='Enter Your Choice'):
                print("Enter roll number in entry your choice column.")
            else:
                res = coll.find({'rollno': entry_choice})   
        elif(rbt_choice == '3'):
            if(entry_choice=='Enter Your Choice'):
                print("Enter roll number in entry your choice column.")
            else:
                res = coll.find({'rollno': entry_choice})   
        elif(rbt_choice == '4'):
            res = coll.find({'hostelv': True }) 
        elif(rbt_choice == '5'):
            res = coll.find({'hostelv': False })   




        # res = coll.find({'hostel':{"$exists":True}})
        co=res.count()
        print(res)
        displayFrame=Frame(self)
        displayFrame.grid(row=9,column=0,sticky="nsew",columnspan=2)
        displayFrame.rowconfigure( 0,weight=1)
        displayFrame.columnconfigure(0,weight=1)
        

        listb = Listbox(displayFrame)
        listb.grid(row=0,column=0,sticky="nsew")
        sb = Scrollbar(displayFrame,orient=VERTICAL,command=listb.yview)
        sb.grid(row=0,column=1,sticky="nsew")
        listb['yscrollcommand'] = sb.set

        
        for i in range(0,co):
            
            listb.insert('end',res[i])