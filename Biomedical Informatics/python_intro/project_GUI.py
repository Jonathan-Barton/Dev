import tkinter as tk
from tkinter import ttk

window = tk.Tk()
import tkinter
from tkinter import *
import csv
import pandas as pd
import time

##read CSV into data frame
data = pd.read_csv(r"C:\Users\jonba\OneDrive\Desktop\Dev\Biomedical Informatics\python_intro\project\patientDataCSV.csv")


mainWindow = tkinter.Tk()
mainWindow.title('Patient Data')
mainWindow.configure(background = '#B3CF00')
mainWindow.geometry('500x500') 

###search MRN fxn, checks for appropriate value 
def searchMRN():
   global mrnLabel
   global mrn
   mrn= mrnEntry.get()
   if int(mrn)>300 or int(mrn) <0:
      deleteButton['state']=NORMAL
      mrnLabel= Label(text= "Not a valid MRN, please try again", bg='red',fg='black')
      mrnLabel.grid(row=2,column=0)
      mrnLabel['state']=DISABLED
      deleteButton['state']=NORMAL
   else:
      global rowDataLabel
      deleteButton['state']=NORMAL
      mrn = int(mrn)
      rowData= data.iloc[mrn-1,:]
      rowDataLabel = Label(bg = 'red', fg='white', text = rowData)
      rowDataLabel.grid(row=2,column=0)


### for the clear button
def deleteText():

   if int(mrn)>300 or int(mrn) <0: 
      mrnLabel.destroy()
   else:
      rowDataLabel.destroy()
   deleteButton['state']=DISABLED
   
   


   
#Pull up patient data
mrnLabel = Label(text ="Search for patient data by MRN", bg='black', fg='#FFCB09')
mrnLabel.grid(row=0,column=0)

###MRN Entry Box
mrnEntry = Entry(borderwidth=3)
mrnEntry.grid(row=1, column=0)
mrnEntry.insert(0,"Enter MRN")

###MRN Button
mrnButton = Button(bg='red', fg='white', text='Search',command= searchMRN)
mrnButton.grid(row=1,column=1)

### delete button
deleteButton = Button(bg = 'red', fg = 'black', text='Clear', command =deleteText)
deleteButton.grid(row=2,column=1)
deleteButton['state']=DISABLED




mainWindow.mainloop()
