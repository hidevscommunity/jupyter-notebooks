import pickle
from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()

def model_prediction(features):
    features = count_vec.transform([features]).toarray()
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/SMS Spam Detection/model/SMS_Spam_Detection_BernoulliNB.pkl', 'rb'))
    Comment = str(list(pickled_model.predict(features)))
    
    return str(f'The message is {Comment}')

message = input('Enter your message')

print(model_prediction(s))

#This may throw error so please prefer the function inside the notebook.
