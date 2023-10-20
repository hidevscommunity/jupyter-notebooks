import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Social_Media_Ads_Classification/model/Social_Media _Ads_prediction_RandomForest.pkl', 'rb'))
    Purchased = str(list(pickled_model.predict(features)))
    
    return str(f'He/She purcased = {Purchased}')


Age = int(input("Enter the age"))
EstimatedSalary = int(input("Enter Salary"))

print(model_prediction([[Age,EstimatedSalary]]))