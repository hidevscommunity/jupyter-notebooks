import pickle
from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()

def model_prediction(features):
    features = count_vec.transform([features]).toarray()
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Spam Detection/model/Spam_Detection_BernoulliNB.pkl', 'rb'))
    Message = str(list(pickled_model.predict(features)))
    
    return str(f'The Comment is {Message}')


message = input('Enter your comment')

print(model_prediction(message))

#This may throw error so please prefer the function inside the notebook.
