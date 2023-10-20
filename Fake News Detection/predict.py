import pickle
from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()

def model_prediction(features):
    features = count_vec.transform([features]).toarray()
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Fake News Detection/model/FakeNews_Detection_BernoulliNB.pkl', 'rb'))
    News = str(list(pickled_model.predict(features)))
    
    return str(f'The News is {News}')

news = input('Enter the news information: -')

print(model_prediction(news))

#This may throw error so please prefer the function inside the notebook.
