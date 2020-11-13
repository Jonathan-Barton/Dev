import random
import csv
import pandas as pd
patientData=[]



x=0
while x < 300:
    
    
    #non-integervariables
    sex = random.choice(["M","F"])
    disease_at_admission2 = random.choice(["D1","D2","D3","D4","D5"])
    state = random.choice(["Utah", "Arizona", "California", "Ohio", "Kansas", "Montana", "Nevada", "Oregon", "Washington", "Maine"]) #random state from 10 chosen states
    comorbidities = random.choice(["C1", "C2", "C3", "C4", "C5"])
    #integer variables
    age = int((random.randrange (18,100)))#random age gen
    visitType = int((random.randrange(1,5)))
    cholesterol = int((random.randrange(150,300)))
    wbcCount = int((random.randrange(4300, 10800)))
    sodium = int((random.randrange(135,145)))
    chloride = int((random.randrange(98,106)))
    bloodSugar = int((random.randrange(70,99)))
    Patient_ID = int(x+1)
    provider_ID = int((random.choice([1,2,3,4,5,6,7,8,9,10])))    #random provider ID between 1-10
    body_temperature = float((round(random.uniform(96.5,99.5),1)))  #random value between 96.5-99.5
    heart_rate = int((random.randrange(60,100)))          #random value between 60-100
    respiratory_rate = int((random.randrange(16,20)))     #random value between 16-20
    #blood_pressure = systolic / diastolic.                      #random value between x/x-x/x --> create independent variables
    systolic_bp = int(random.randrange(100,170))
    diastolic_bp = int(random.randrange(70,110))
    weight = int((random.randrange (100,375)))#random weight get
    height_in = int((random.randrange(60,80)))
    bmi = float(round((((weight/(height_in**2)) * 703)), 2))
    
    
    
    
    
    
    
    
    dict1= {'Weight': weight, "Height in Inches": height_in, "BMI": bmi, 'Patient ID': Patient_ID, 'Sex': sex, 'Disease at Admission': disease_at_admission2, 'Age': age, 'Visit Type': visitType, 'Cholesterol': cholesterol, 'WBC Count': wbcCount, 'Sodium': sodium, 'Chloride': chloride, 'Blood Sugar': bloodSugar, 'State': state, 'Provider ID': provider_ID, 'body temperature': body_temperature, 'heart rate': heart_rate, 'respiratory rate': respiratory_rate, 'systolic BP': systolic_bp, 'diastolic BP': diastolic_bp, 'comorbidities': comorbidities} #creates new dictionary each loop
    patientData.append(dict1) #appends new dict1 each loop
    x+=1
    
import pandas as pd 
patientDataCSV = pd.DataFrame(patientData)

patientDataCSV.to_csv('patientDataCSV.csv', index=False)

print(patientDataCSV)