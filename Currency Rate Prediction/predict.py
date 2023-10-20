import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/currency_rate_prediction/model/currency-exchange-rate-prediction_DTR.pkl', 'rb'))
    Close = str(list(pickled_model.predict(features)))
    
    return str(f'The Close amount is {Close}')

Open = float(input("Enter Open value"))
High = float(input("Enter High value"))
Low = float(input("Enter Low value"))

print(model_prediction([[Open,High,Low]]))