import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Mobile Price Classification/model/Mobile_Price_Prediction_LogisticRegression.pkl', 'rb'))
    Price = str(list(pickled_model.predict(features)))
    
    return str(f'The Mobile Price is {Price}')

battery_power = int(input("Enter the Battery Power: -"))
blue = int(input("Blue color or not: -"))
clock_speed = float(input("Enter the clock speed: -"))
dual_sim = int(input("Dual Sim or not: -"))
fc = int(input("Want feature cellular charger or not: -"))
four_g = int(input("4G or not: -"))
int_memory = int(input("Enter the internal memory: -"))
m_dep = float(input("Enter the mdep: -"))
mobile_wt = int(input("Enter the mobile weight: -"))
n_cores = int(input("Enter number of cores: - "))
pc = int(input("Enter the number of pc: -"))
px_height = int(input("Enter the pixel height: -"))
px_width = int(input("Enter the pixel width: -"))
ram = int(input("Enter RAM: -"))
sc_h = int(input("Enter sc_h: -"))
sc_w = int(input('Enter sc_w: -'))
talk_time = int(input("Enter Talktime: -"))
three_g = int(input("Want 3G or not: -"))
touch_screen = int(input('Want touch screen or not: -'))
wifi = int(input("Want Wifi Support or not: -"))

print(model_prediction([[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]]))
