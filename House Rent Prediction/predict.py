import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/House_rent_prediction/model/House_rent_prediction_linearregression.pkl', 'rb'))
    Rent = str(list(pickled_model.predict(features)))
    
    return str(f'The Rent is {Rent}')

BHK = int(input("Enter BHK"))
Size = int(input("Enter Size"))
Area_Type = int(input("Enter Area type"))
Area_Locality = int(input("Enter Area Locality"))
City = int(input("Enter City"))
Furnishing_Status = int(input("Enter Furnishing Status"))
Tenant_Preferred = int(input("Enter Tenant Preferred"))
Bathroom = int(input("Enter number of Bathroom"))
Point_of_Contact = int(input("Enter Point of Contact"))

print(model_prediction([[BHK,Size,Area_Type,Area_Locality,City,Furnishing_Status,Tenant_Preferred,Bathroom,Point_of_Contact]]))