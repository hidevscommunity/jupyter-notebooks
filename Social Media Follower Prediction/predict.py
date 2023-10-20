import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Social Media Follower Prediction/model/Social_Media_Followers_Linear.pkl', 'rb'))
    Followers = str(list(pickled_model.predict(features)))
    
    return str(f'The next month followers will be : {Followers}')


followers_lost = int(input("Number of followers lost:-"))
followers_net = int(input("Number of net followers:-"))
followers_total = int(input("Total Number of followers:-"))
subscribers_gained = int(input("Number of subscribers gained:-"))
subscribers_lost = int(input("Number of subscribers lost:-"))
subscribers_net = int(input("Number of net subscribers:-"))
subscribers_total = int(input("Total Number of Subscribers:-"))
views = int(input("Total Number of views:-"))

print(model_prediction([[followers_lost,followers_net,followers_total,subscribers_gained,subscribers_lost,subscribers_net,subscribers_total,views]]))