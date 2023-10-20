import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\Dogecoin_price_Prediction_li.pkl', 'rb'))
    Close = str(pickled_model.predict(features)[0][0])
    
    return str(f'The dogecoin price is {Close}')

o=float(input("Enter the openning amount: - "))
h=float(input("Enter the high amount: - "))
l=float(input("Enter the low amount: - "))
ad=float(input("Enter the adj close: - "))
v=float(input("Enter the volume: - "))

print(model_prediction([[o,h,l,ad,v]]))