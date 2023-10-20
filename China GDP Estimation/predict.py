import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\china_gdp_estimate_rr.pkl', 'rb'))
    ch = str(pickled_model.predict(features)[0])
    
    return str(f'The china estimate GDP is {ch}')

Y_2000 = float(input("Enter the GDP of year 2000: "))
Y_2001 = float(input("Enter the GDP of year 2001: "))
Y_2002 = float(input("Enter the GDP of year 2002: "))
Y_2003 = float(input("Enter the GDP of year 2003: "))
Y_2004 = float(input("Enter the GDP of year 2004: "))
Y_2005 = float(input("Enter the GDP of year 2005: "))
Y_2006 = float(input("Enter the GDP of year 2006: "))
Y_2007 = float(input("Enter the GDP of year 2007: "))
Y_2008 = float(input("Enter the GDP of year 2008: "))
Y_2009 = float(input("Enter the GDP of year 2009: "))
Y_2010 = float(input("Enter the GDP of year 2010: "))
Y_2011 = float(input("Enter the GDP of year 2011: "))
Y_2012 = float(input("Enter the GDP of year 2012: "))
Y_2013 = float(input("Enter the GDP of year 2013: "))
Y_2014 = float(input("Enter the GDP of year 2014: "))
Y_2015 = float(input("Enter the GDP of year 2015: "))
Y_2016 = float(input("Enter the GDP of year 2016: "))
Y_2017 = float(input("Enter the GDP of year 2017: "))
Y_2018 = float(input("Enter the GDP of year 2018: "))
Y_2019 = float(input("Enter the GDP of year 2019: "))
Y_2020 = float(input("Enter the GDP of year 2020: "))

model_prediction([[Y_2000, Y_2001, Y_2002, Y_2003, Y_2004, Y_2005, Y_2006, Y_2007, Y_2008, Y_2009,Y_2010,Y_2011,Y_2012,Y_2013,Y_2014,Y_2015,Y_2016,Y_2017,Y_2018,Y_2019,Y_2020]])