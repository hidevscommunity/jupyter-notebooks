import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\\bike_share_demand_pred_li.pkl', 'rb'))
    bi = str(round(pickled_model.predict(features)[0][0]))
    
    return str(f'The bike demand are {bi}')

season = int(input("Enter the season: "))
holiday = int(input("Enter the holiday: "))
workingday = int(input("Enter the number of working day: "))
weather = int(input("Enter the weather: "))
temp = float(input("Enter the temp: "))
atemp = float(input("Enter the atemp: "))
humidity =  int(input("Enter the humidity: "))
windspeed = float(input("Enter the wind speed: "))
casual = int(input("Enter the number of non-registered user rentals initiated: "))
registered = int(input("Enter the number of registered user rentals initiated: "))

print(model_prediction([[season, holiday, workingday, weather, temp, atemp, humidity, windspeed, casual, registered]]))