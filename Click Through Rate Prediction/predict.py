import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Click_through_prediction_RandomForest.pkl', 'rb'))
    Clicked = str(list(pickled_model.predict(features)))
    
    return str(f'Clicked on Ad {Clicked}')

Daily_Time_Spent_on_Site = int(input())
Age = int(input())
Daily_Internet_Usage = int(input())
Gender = int(input())
Area_income = int(input())

print(model_prediction([[Daily_Time_Spent_on_Site,Age,Daily_Internet_Usage,Gender,Area_income]]))