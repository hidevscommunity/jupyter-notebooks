import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('crime_prediction_rr.pkl', 'rb'))
    crime = str(list(pickled_model.predict(features)))
    
    return str(f'The crime analysis is {crime}')

year = int(input("Enter the year: - "))
month = int(input("Enter the month: - "))
day = int(input("Enter the day: - "))
hour = int(input("Enter the hour: - "))
dayofyear = int(input("Enter the day of year: - "))
week = int(input("Enter the week: - "))
weekofyear = int(input("Enter the week of year: - "))
dayofweek =  int(input("Enter the day of week: - "))
weekday = int(input("Enter the weekday: - "))
quarter = int(input("Enter the quarter: - "))
latitude = float(input("Enter the latitude: - "))
longitude = float(input("Enter the longitude: - "))

print(model_prediction([[year,month,day,hour,dayofyear,week,weekofyear,dayofweek,weekday,quarter,latitude,longitude]]))