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

################# PROVIDER ROW ######################################################!!!!!!

###search Patient ID fxn, checks for appropriate value 
def searchProviders():
   global providerLabel
   global provider
   provider= providerEntry.get()
   if int(provider)>10 or int(provider) <0:
      deleteButtonP['state']=NORMAL
      providerLabel= Label(text= "Not a valid Provider ID, please try again", bg='red',fg='black')
      providerLabel.grid(row=2,column=5)
      providerLabel['state']=DISABLED
      deleteButton['state']=NORMAL
   else:
      global rowDataLabel
      deleteButtonP['state']=NORMAL
      provider = int(provider)
      rowDataP= data.keys[provider-1,:] #get the thing fromt the row
      rowDataLabelP = Label(bg = 'blue', fg='white', text = rowDataP)
      rowDataLabelP.grid(row=2,column=5)

### for the clear button
def deleteProviderText():

   if int(provider)>300 or int(provider) <0: 
      providerLabel.destroy()
   else:
      rowDataLabelP.destroy()
   deleteButtonP['state']=DISABLED

   
#Pull up patient data
providerLabel = Label(text ="Search for patients using Provider ID", bg='black', fg='#FFCB09')
providerLabel.grid(row=0,column=5)

###MRN Entry Box
providerEntry = Entry(borderwidth=3)
providerEntry.grid(row=1, column=5)
providerEntry.insert(0,"Enter Provider ID")

###MRN Button
providerButton = Button(bg='blue', fg='white', text='Search',command= searchProviders)
providerButton.grid(row=1,column=6)

### delete button
deleteButtonP = Button(bg = 'blue', fg = 'black', text='Clear', command =deleteProviderText)
deleteButtonP.grid(row=2,column=6)
deleteButtonP['state']=DISABLED



mainWindow.mainloop()