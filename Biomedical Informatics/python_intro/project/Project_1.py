import random
#import numpy as np

patientList = [] #list where dictionaries are stored

co_list = ["C1", "C2", "C3", "C4", "C5"]
patient_states = ["Utah", "Arizona", "California", "Ohio", "Kansas", "Montana", "Nevada", "Oregon", "Washington", "Maine"]
patient = 1
#we need to create data for 1-300 patient IDs

#change the value of n based on user input. for ___ in (userinput)

while patient < 300:
    state = random.choice(patient_states) #random state from 10 chosen states
    provider_ID = (random.choice([1,2,3,4,5,6,7,8,9,10]))    #random provider ID between 1-10
    #vital signs 4x in a range
    body_temperature = (round(random.uniform(96.5,99.5),1))  #random value between 96.5-99.5
    heart_rate = (random.randint(60,100))          #random value between 60-100
    respiratory_rate = (random.randint(16,20))     #random value between 16-20
    #blood_pressure = cystolic / diastolic.                      #random value between x/x-x/x --> create independent variables
    systolic_bp = random.randint(100,170)
    diastolic_bp = random.randint(70,110)
    comorbidities = random.choice(co_list)
    dict1= {'State': state, 'Provider ID': provider_ID, 'body temperature': body_temperature, 'heart rate': heart_rate, 'respiratory rate': respiratory_rate, "systolic BP": systolic_bp, "diastolic BP": diastolic_bp, "comorbidities": comorbidities} 
    patientList.append(dict1) #appends new dict1 each loop --> mesh all of our random generators together
    patient = patient + 1
    print(patientList)

