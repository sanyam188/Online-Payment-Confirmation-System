from tkinter import *
from tkinter import ttk

class View(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        choice= StringVar()
        rbt1=Radiobutton(self,text='Name',variable=choice,value='1')
        rbt2=Radiobutton(self,text='Branch',variable=choice,value='2')
        rbt3=Radiobutton(self,text='Floor',variable=choice,value='3')
        rbt4=Radiobutton(self,text='Branch',variable=choice,value='4')
        rbt5=Radiobutton(self,text='Roll Number',variable=choice,value='5')      
        rbt6=Radiobutton(self,text='Room Number',variable=choice,value='6')
        
        rbt1.grid(row=1,column=0,sticky="nsew")
        rbt2.grid(row=2,column=0,sticky="w")
        rbt3.grid(row=3,column=0,sticky="w")
        rbt4.grid(row=4,column=0,sticky="w")
        rbt5.grid(row=5,column=0,sticky="w")
        rbt6.grid(row=6,column=0,sticky="w")
        op=StringVar()
        opp=StringVar()
        entrybtn = Entry(self,textvariable=op)
        entrybtn.grid(row=7,column=1,sticky="nsew")
        op.set("Enter Your Choice")
        def callback():
            opp=op.get()
        submitbtn = Button(self,command=callback,text="Submit").grid(row=8,column=1)
        print(opp,choice)

        self.rowconfigure( 0,weight=1)
        self.rowconfigure( 1,weight=1)
        self.rowconfigure( 2,weight=1)
        self.rowconfigure( 3,weight=1)
        self.rowconfigure( 4,weight=1)
        self.rowconfigure( 5,weight=1)
        self.rowconfigure( 6,weight=1)
        self.rowconfigure( 7,weight=2)
        self.rowconfigure( 8,weight=3)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        
        # lbl = ttk.Label(self,text = "View Page")
        # lbl.grid()
