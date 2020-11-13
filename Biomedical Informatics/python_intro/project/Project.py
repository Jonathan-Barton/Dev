
#Tiegen doin stuff
​import random
import csv
patientList = []#list where dictionaries are stored
​
x=0
while x<300:#generate 300 patients 
    age = (random.randrange (18,100))#random age gen
    weight = (random.randrange (100,375))#random weight gen
    mrn = x+1 # so MRN doesn't start at 0
    height_in = (random.randrange(48,78)) #assign height
    bmi = float("{:.1f}".format((((weight/(height_in**2)) * 703))))### bmi calc
    dict1= {'Age': age, 'Weight': weight, 'MRN': mrn, 'Height': height_in, 'BMI': bmi} #creates new dictionary each loop
    patientList.append(dict1) #appends new dict1 each loop 
    x+=1
    
#print(patientList[int(input("input MRN"))-1])#-1 to put input back to patientList index numbers for print function
​
​
keys = patientList[0].keys()#sets keys variable dictionary keys
with open('peopleDataset.csv', 'w', newline='')  as output_file:#opens csv tool, output file
    dict_writer = csv.DictWriter(output_file, keys)#dict_writet variable declared. Makes file
    dict_writer.writeheader()#writes header with keys
    dict_writer.writerows(patientList)#writes data rows 