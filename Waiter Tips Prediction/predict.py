import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Waiter_tips_Prediction/model/Waiter_tips_Prediction_linear.pkl', 'rb'))
    tip = str(list(pickled_model.predict(features)))
    
    return str(f'The amount of the tip is {tip}')

total_bill = float(input("Enter Bill Amount"))
sex = float(input("Enter sex"))
size = float(input("Enter size"))
day = float(input("Enter day"))
time = float(input("Enter time"))
smoker = int(input("Enter smoker"))

print(model_prediction([[total_bill,sex,size,day,time,smoker]]))