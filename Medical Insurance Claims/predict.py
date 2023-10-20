import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\medical_insurance_pred_rr.pkl', 'rb'))
    mi = str(pickled_model.predict(features)[0])
    
    return str(f'The medical insurance price is {mi}')

age = int(input("Enter the age: "))
sex = int(input("Enter the gender: "))
bmi = float(input("Enter the bmi: "))
children = int(input("Enter the number of children: "))
smoker = int(input("Enter whether smoker or not: "))
region = int(input("Enter the region: "))

print(model_prediction([[age, sex, bmi, children, smoker, region]]))