import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Insurance_Prediction_kn.pkl', 'rb'))
    TravelInsurance = str(pickled_model.predict(features)[0])
    if TravelInsurance=='1':
        TravelInsurance='taken by person'
    else:
        TravelInsurance='not taken by person'
    
    return str(f'The Travel Insurance is {TravelInsurance}')

Age = int(input("Enter the age of person: - "))
EmploymentType = int(input("Enter the employee type of person: - "))
GraduateOrNot = int(input("Enter whether the employee is graduate or not: - "))
AnnualIncome = int(input("Enter the annual income of employee: - "))
FamilyMembers = int(input("Enter the number of family members: - "))
FrequentFlyer = int(input("Enter whether the person is frequent flyer or not: - "))
EverTravelledAbroad = int(input("Enter whether the person is ever travelled or not: - "))

print(model_prediction([[Age, EmploymentType, GraduateOrNot, AnnualIncome, FamilyMembers, FrequentFlyer, EverTravelledAbroad]]))