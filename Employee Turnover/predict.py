import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Employee_turnover/model/Employee_Turnover_prognosis_RandomForest.pkl', 'rb'))
    event = str(list(pickled_model.predict(features)))
    
    return str(f'The event is {event}')

stag = float(input("Enter stag"))
gender = int(input("Enter gender"))
age = float(input("Enter age"))
industry = int(input("Enter industry"))
profession = int(input("Enter profession"))
traffic = int(input("Enter traffic"))
coach = int(input("Enter coach"))
head_gender = int(input("Enter head gender"))
greywage = int(input("Enter greywage"))
way = int(input("Enter way"))
extraversion = float(input("Enter extraversion"))
independ = float(input("Enter independ"))
selfcontrol = float(input("Enter selfcontrol"))
anxiety = float(input("Enter anxiety"))
novator = float(input("Enter novator"))

print(model_prediction([[stag,gender,age,industry,profession,traffic,coach,head_gender,greywage,way,extraversion,independ,selfcontrol,anxiety,novator]]))