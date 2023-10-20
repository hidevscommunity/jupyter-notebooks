import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Online_food_order/model/online_food_order_prediction_RandomForest.pkl', 'rb'))
    Output = str(list(pickled_model.predict(features)))
    
    return str(f'The output is {Output}')

Age = int(input("Enter Age"))
Gender = int(input("Enter gender"))
Marital_Status = int(input("Enter marital status"))
Occupation = int(input("Enter occupation"))
Monthly_Income = int(input("Enter monthly income"))
Educational_Qualifications = int(input("Enter education qualification"))
Family_size = int(input("Enter Family size"))
latitude = float(input("Enter latitude"))
longitude = float(input("Enter longitude"))
Pincode = int(input("Enter pincode"))
Feedback = int(input("Enter feedback"))

print(model_prediction([[Age,Gender,Marital_Status,Occupation,Monthly_Income,Educational_Qualifications,Family_size,latitude,longitude,Pincode,Feedback]]))