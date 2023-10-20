import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Video_game_sales_prediction/model/Sales_Prediction_LinearRegresssion.pkl', 'rb'))
    Global_Sales_up = str(list(pickled_model.predict(features)))
    
    return str(f'The Sale is {Global_Sales_up}')

Rank = int(input("Enter Rank"))
Platform = float(input("Enter Platform"))
Year = float(input("Enter Year"))
Genre = int(input("Enter Genre"))
Publisher = int(input("Enter Publisher"))
NA_Sales_up = float(input("Enter NA Sales"))
EU_Sales_up = float(input("Enter EU Sales"))
JP_Sales_up = float(input("Enter JP Sales"))
Other_Sales_up = float(input("Enter Other Sales"))

print(model_prediction([[Rank, Platform, Year, Genre, Publisher, NA_Sales_up, EU_Sales_up, JP_Sales_up, Other_Sales_up]]))