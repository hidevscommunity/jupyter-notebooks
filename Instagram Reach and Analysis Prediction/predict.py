import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Instagram Reach and Analysis Prediction/model/Instagrm_Reach_RandomRegressor.pkl', 'rb'))
    Impression = str(list(pickled_model.predict(features)))
    
    return str(f'The Impressions on your account are:- {Impression}')

Likes = int(input("Enter number of Likes:-"))
Saves = int(input("Enter number of Saves:-"))
Comments = int(input("Enter number of Comments:-"))
Shares = int(input("Enter number of Shares:-"))
Profile_Visits = int(input("Enter number of Profile Visits:-"))
Follows = int(input("Enter number of Follows:-"))

print(model_prediction([[Likes,Saves, Comments, Shares,Profile_Visits,Follows]]))