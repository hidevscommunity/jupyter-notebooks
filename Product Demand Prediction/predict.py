import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Product_Demand_dt.pkl', 'rb'))
    units = str(pickled_model.predict(features)[0])
    
    return str(f'The number of units solds is {units}')

Store_ID = int(input("Enter the store id: "))
Total_Price = float(input("Enter the total price: "))
Base_Price = float(input("Enter the base price: "))

print(model_prediction([[Store_ID, Total_Price, Base_Price]]))