from tkinter import *
from tkinter import ttk
from updatedb import UpdateDocuments
from option_view import View
class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1000x500")
        container=ttk.Frame(self)
        container.grid(row=0,column=0,sticky="nsew",padx=5, pady=5)
        optionFrame=ttk.Frame(container,relief=RAISED,borderwidth = 1)
        otherFrame=ttk.Frame(container,relief=SUNKEN)   
         
        update = ttk.Button(optionFrame,text="Update",command=lambda:self.update(otherFrame))
        view = ttk.Button(optionFrame,text="View",command=lambda:self.view(otherFrame))
        search =ttk.Button(optionFrame,text="Search File")
        upload =ttk.Button(optionFrame,text="Upload File")
        optionFrame.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)
        otherFrame.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)
        update.grid(column=0,row=1,sticky="nsew")
        view.grid(column=0,row=2,sticky="nsew")
        search.grid(column=0,row=3,sticky="nsew")
        upload.grid(column=0,row=0,sticky="nsew")
       
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        container.columnconfigure(1,weight=4)
        optionFrame.rowconfigure(0,weight=1)
        optionFrame.rowconfigure(1,weight=2)
        optionFrame.rowconfigure(2,weight=2)
        optionFrame.rowconfigure(3,weight=2)
        optionFrame.rowconfigure(4,weight=2)
        optionFrame.rowconfigure(5,weight=60)
        optionFrame.columnconfigure(0,weight=1)
        otherFrame.columnconfigure(0,weight=1)
        otherFrame.rowconfigure(0,weight=1)

        lbl = Label(otherFrame, text="Welcome")
        lbl.grid(row=0,column=0,sticky="nsew")

        # tryFrame = ttk.Frame(otherFrame,relief=SUNKEN)
        # tryFrame.grid(row=0,column=0,sticky="nsew",padx=25,pady=25)
        # tryFrame.rowconfigure(0,weight=1)
        # tryFrame.columnconfigure(0,weight=1)
        # choice = StringVar()
        # rbt1=Radiobutton(tryFrame,text='Roll Number',variable=choice,value='1')
        # rbt2=Radiobutton(tryFrame,text='Branch',variable=choice,value='2')
        # rbt1.grid(row=0,column=0,sticky="w")
        # rbt2.grid(row=1,column=1)        
        # tryFrame.rowconfigure(0,weight=1)
        # tryFrame.rowconfigure(1,weight=1)
        # tryFrame.rowconfigure(2,weight=1)
        # tryFrame.rowconfigure(3,weight=1)
        # tryFrame.rowconfigure(4,weight=1)
        # tryFrame.columnconfigure(0,weight=1)
        # tryFrame.columnconfigure(2,weight=1)
        # tryFrame.columnconfigure(3,weight=1)
        # tryFrame.columnconfigure(1,weight=1)

        # self.frame={}
        # for F in (View,Update):
        #     page = F.__name__
        #     frames = F(parent=otherFrame, controller=self)
        #     self.frame[page]=frames
        #     frames.grid(row=0,column=0,sticky="nsew")
        # self.show("View")

    def view(self,otherFrame):
        dd = View(parent=otherFrame, controller=self)
        dd.grid(row=0,column=0,sticky="nsew")
        dd.tkraise()

    def update(self,otherFrame):
        dd = Update(parent=otherFrame, controller=self)
        dd.grid(row=0,column=0,sticky="nsew")
        dd.tkraise()

    # def show(self,page):
    # self.frame[page].tkraise()


class Update(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        updt = UpdateDocuments()
        lbl = ttk.Label(self,text = "Elements in the Database are Up to date with the excel file.")
        lbl.grid()


if __name__ == "__main__":
    app=SampleApp()
    app.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# mainFrame = ttk.Frame(root,relief="raised",padding=(4,4,4,4))
# optionFrame = ttk.Labelframe(mainFrame,text="Options")
# otherFrame = ttk.Frame(mainFrame)
# extraFrame = ttk.Frame(optionFrame)
# update = ttk.Button(optionFrame,text="Update")
# view = ttk.Button(optionFrame,text="View")
# search = ttk.Button(optionFrame,text="Search File")
# lbl = ttk.Label(otherFrame, text="Just")
# s = ttk.Separator(mainFrame,orient=HORIZONTAL)

# mainFrame.grid(column=0,row=0,sticky=(N, S, E, W))
# optionFrame.grid(column=0,row=0,sticky=(N, S, E, W))
# otherFrame.grid(column=1,row=0,sticky=(N, S, E, W))
# update.grid(column=0,row=1,sticky=(N, S, E, W))
# view.grid(column=0,row=2,sticky=(N, S, E, W))
# search.grid(column=0,row=3,sticky=(N, S, E, W))
# extraFrame.grid(column=0,row=4,sticky=(N, S, E, W))
# lbl.grid(column=2,row=1)
# s.grid(column=1)

# root.rowconfigure(0,weight=1)
# root.columnconfigure(0,weight=1)
# mainFrame.rowconfigure(0,weight=2)
# mainFrame.rowconfigure(1,weight=2)
# mainFrame.rowconfigure(2,weight=2)
# mainFrame.rowconfigure(3,weight=2)
# mainFrame.rowconfigure(4,weight=5)
# mainFrame.columnconfigure(0,weight=1)
# mainFrame.columnconfigure(1,weight=5)
# optionFrame.rowconfigure(0,weight=2)
# optionFrame.rowconfigure(1,weight=2)
# optionFrame.rowconfigure(2,weight=2)
# optionFrame.rowconfigure(3,weight=2)
# optionFrame.rowconfigure(4,weight=7)
# optionFrame.columnconfigure(0,weight=1)
# root.mainloop()