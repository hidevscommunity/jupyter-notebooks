import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('electricity_price_pred_rr.pkl', 'rb'))
    ele = str(pickled_model.predict(features)[0])
    
    return str(f'The electricity price is {ele}')

DayOfWeek = float(input("Enter the daf od week: - "))
WeekOfYear = float(input("Enter the week of year: - "))
Year = float(input("Enter the year: - "))
PeriodOfDay = float(input("Enter the period of day: - "))
ForecastWindProduction = float(input("Enter the ForecastWindProduction: - "))
SystemLoadEA = float(input("Enter the SystemLoadEA: - "))
SMPEA =  float(input("Enter the SMPEA: - "))
ORKWindspeed = float(input("Enter the ORKWindspeed: - "))
CO2Intensity = float(input("Enter the CO2Intensity: - "))
ActualWindProduction = float(input("Enter the ActualWindProduction: - "))
SystemLoadEP2 = float(input("Enter the SystemLoadEP2: - "))

print(model_prediction([[DayOfWeek, WeekOfYear, Year, PeriodOfDay, ForecastWindProduction, SystemLoadEA, SMPEA, ORKWindspeed, CO2Intensity, ActualWindProduction, SystemLoadEP2]]))