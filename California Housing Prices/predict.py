import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/California_housing_prices/model/california_housing_prices_LinearRegression.pkl', 'rb'))
    median_house_value = str(list(pickled_model.predict(features)))
    
    return str(f'The Price is {median_house_value}')

longitude = float(input("Enter longitude"))

latitude = float(input("Enter latitude"))

total_rooms = int(input("Enter total rooms"))

total_bedrooms = float(input("Enter total bedrooms"))

population = int(input("Enter population"))

households = int(input("Enter households"))

median_income = float(input("Enter median income"))

ocean_proximity = int(input("Enter Ocean proximity"))

print(model_prediction([[longitude,latitude,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity]]))