from pymongo import MongoClient
from tkinter import *

import xlwt
from xlwt import Workbook
from tkinter import filedialog
class Write(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        wb = Workbook() 
  

        sheet1 = wb.add_sheet('Sheet 1') 
        
        sheet1.write(1, 0, 'ISBT DEHRADUN') 
        sheet1.write(2, 0, 'SHASTRADHARA') 
        sheet1.write(3, 0, 'CLEMEN TOWN') 
        sheet1.write(4, 0, 'RAJPUR ROAD') 
        sheet1.write(5, 0, 'CLOCK TOWER') 
        sheet1.write(0, 1, 'ISBT DEHRADUN') 
        sheet1.write(0, 2, 'SHASTRADHARA') 
        sheet1.write(0, 3, 'CLEMEN TOWN') 
        sheet1.write(0, 4, 'RAJPUR ROAD') 
        sheet1.write(0, 5, 'CLOCK TOWER') 
        
        filename = filedialog.asksaveasfilename()
        wb.save(filename) 
