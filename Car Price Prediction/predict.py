import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Car Price Prediction/model/Car_Price_Prediction_LinearRegression.pkl', 'rb'))
    Price = str(list(pickled_model.predict(features)))
    
    return str(f'The Price is {Price}')

symboling = int(input("Enter the symboling"))
CarName= int(input("Enter the Car Name in numeric between 1-20"))
fueltype=int(input("Enter the fueltype"))
aspiration=int(input("Enter the aspiration"))
carbody =int(input("Enter the carbody"))
drivewheel=int(input("Enter the drivewheel"))
enginelocation=int(input("Enter the enginelocation"))
wheelbase=float(input("Enter the wheelbase"))
carlength=float(input("Enter the carlength"))
carwidth=float(input("Enter the carwith"))
carheight=float(input("Enter the carheight"))
curbweight=int(input("Enter the curbweight"))
enginesize=int(input("Enter the enginesize"))
fuelsystem=input(input("Enter the fuelsystem"))
boreratio=float(input("Enter the boreratio"))
horsepower=int(input("Enter the horsepower"))
peakrpm=int(input("Enter the peakrpm"))
citympg=int(input("Enter the citympg"))
highwaympg=int(input("Enter the highwaympg"))    

print(model_prediction([[symboling,CarName,fueltype,aspiration,carbody,drivewheel,enginelocation,wheelbase,carlength,carwidth,carheight,curbweight,enginesize,fuelsystem,
boreratio,peakrpm,citympg,highwaympg]]))