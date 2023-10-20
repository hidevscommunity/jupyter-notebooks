import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\stock_prediction_li.pkl', 'rb'))
    Close = str(pickled_model.predict(features)[0][0])
    
    return str(f'The close is {Close}')

d=float(input("Enter the date: - "))
o=float(input("Enter the openning amount: - "))
h=float(input("Enter the high amount: - "))
l=float(input("Enter the low amount: - "))
v=float(input("Enter the volume: - "))
n=float(input("Enter the name: - "))

print(model_prediction([[d,o,h,l,v,n]]))