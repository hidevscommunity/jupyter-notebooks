import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Student grade performance model/model/StudentGradesPrediction_LinearRegresssion.pkl', 'rb'))
    Stgrades = str(list(pickled_model.predict(features)))
    
    return str(f'He/She got grade = {Stgrades}')


school = int(input("enter school"))
sex = int(input("enter sex"))          
age = int(input("enter age"))        
famsize = int(input("enter famsize"))     
Pstatus = int(input("enter Pstatus"))    
Medu = int(input("enter Medu"))     
Fedu = int(input("enter Fedu"))        
Mjob = int(input("enter Mhob"))       
Fjob = int(input("enter Fjob"))        
reason = int(input("enter reason"))       
guardian = int(input("enter guardian"))     
traveltime = int(input("enter traveltime"))   
studytime = int(input("enter studytime"))    
failures = int(input("enter failures"))    
schoolsup = int(input("enter schoolsup"))
famsup = int(input("enter famsup"))      
paid= int(input("enter paid"))         
activities = int(input("enter activities"))  
nursery = int(input("enter nursery"))   
higher= int(input("enter higher"))       
internet = int(input("enter internet"))    
famrel= int(input("enter famrel"))
freetime = int(input("enter freetime"))  
goout= int(input("enter goout"))        
Dalc= int(input("enter dalc"))         
Walc= int(input("enter walc"))        
health =int(input("enter health"))        
absences = int(input("enter absence"))      
G1= int(input("enter G1"))
G2=int(input("enter G2"))  


print(model_prediction([[school,sex,age,famsize,Pstatus,Medu,Fedu,Mjob,Fjob,reason,guardian,traveltime,studytime,failures,schoolsup,famsup,paid,activities,nursery,higher,internet,famrel,freetime,goout,Dalc,Walc,health,absences,G1,G2]]))