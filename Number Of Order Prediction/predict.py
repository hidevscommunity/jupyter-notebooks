import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Number_of_order_prediction/model/Number_of_orders_Prediction_LinearRegression.pkl', 'rb'))
    Price = str(list(pickled_model.predict(features)))
    
    return str(f'The Price is {Price}')

Store_id = int(input("Enter store id"))
Store_Type = int(input("Enter store type"))
Location_Type = int(input("Enter location type"))
Region_Code = int(input("Enter region code"))
Date = int(input("Enter store date"))
Holiday = int(input("Enter holiday"))
Discount = int(input("Enter discount"))
Order = int(input("Order"))

print(model_prediction([[Store_id,Store_Type,Location_Type,Region_Code,Date,Holiday,Discount,Order]]))