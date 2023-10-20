import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\TATA_Motors_Stock_Prediction_li.pkl', 'rb'))
    Close = str(pickled_model.predict(features)[0][0])
    
    return str(f'The TATA motors stock price is closed at {Close}')

o=float(input("Enter the opening amount: - "))
h=float(input("Enter the high amount: - "))
l=float(input("Enter the low amount: - "))
v=float(input("Enter the volume: - "))

print(model_prediction([[o,h,l,v]]))