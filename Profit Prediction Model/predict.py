import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Profit_Prediction_Model/model/Profit_Prediction_LinearRegresssion.pkl','rb'))
    Profit = str(list(pickled_model.predict(features)))
    
    return str(f'The Profit is {Profit}')

RD_Spend = float(input("Enter R&D Spend"))
Administration = float(input("Enter the Administration"))
Marketing_Spend = float(input("Enter the Marketing Spend"))
State = int(input("Enter the State in number"))
print(model_prediction([[RD_Spend, Administration, Marketing_Spend, State]]))