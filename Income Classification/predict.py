import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\Income_classification_ra.pkl', 'rb'))
    ic = str(pickled_model.predict(features)[0])
    if ic=='1':
        ic='greater then 50000'
    else:
        ic='less then or equal to 50000'
    
    return str(f'The income is {ic}')


age = int(input("Enter the age: "))
workclass = int(input("Enter the work class: "))
fnlwgt = int(input("Enter the fnlwgt: "))
education = int(input("Enter the education: "))
education_num = int(input("Enter the education number: "))
marital_status = int(input("Enter the martial status: "))
occupation = int(input("Enter the occupation: "))
relationship = int(input("Enter the relationship: "))
race = int(input("Enter the race: "))
sex = int(input("Enter the sex: "))
capital_gain = int(input("Enter the capital gain: "))
capital_loss = int(input("Ente the capital loss: "))
hours_per_week = int(input("Enter the hour per week: "))
native_country = int(input("Enter the native country: "))

print(model_prediction([[age, workclass, fnlwgt, education, education_num, marital_status, occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country]]))