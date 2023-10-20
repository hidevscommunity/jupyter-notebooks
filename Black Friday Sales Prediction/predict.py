import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\\black_friday_sales_pred_rr.pkl', 'rb'))
    bl = str(pickled_model.predict(features)[0])
    
    return str(f'The black friday sales is {bl}')

User_ID = float(input("Enter the user id: "))
Product_ID = float(input("Enter the product id: "))
Gender = float(input("Enter the gender: "))
Age = float(input("Enter the age: "))
Occupation = float(input("Enter the occupation: "))
City_Category = float(input("Enter the city category: "))
Stay_In_Current_City_Years = float(input("Enter the number of years stay in city: "))
Marital_Status = float(input("Enter the marital status"))
Product_Category_1 = float(input("Enter the product category 1: "))
Product_Category_2 = float(input("Enter the product category 2: "))
Product_Category_3 = float(input("Enter the product category 3: "))

print(model_prediction([[User_ID, Product_ID,Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status, Product_Category_1, Product_Category_2, Product_Category_3]]))