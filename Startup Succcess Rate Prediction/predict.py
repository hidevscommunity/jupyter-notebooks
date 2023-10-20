import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\Startup_Success_Rate_Pred_ra.pkl', 'rb'))
    s = str(pickled_model.predict(features)[0])
    if s=='1':
        s='closed'
    else:
        s='acquired'
    
    return str(f'The startup will {s}')

state_code = int(input("Enter the state code: "))
name = int(input("Enter the name: "))
labels = int(input("Enter the labels: "))
founded_at = int(input("Enter the founded date: "))
closed_at = int(input("Enter the closed date: "))
category_code = int(input("Enter the category code: "))
is_mobile = int(input("Enter whether the startup is mobile or not: "))
is_gamesvideo = int(input("Enter whether the startup is gamesvedio or not: "))

print(model_prediction([[state_code, name, labels, founded_at, closed_at, category_code, is_mobile,is_gamesvideo]]))