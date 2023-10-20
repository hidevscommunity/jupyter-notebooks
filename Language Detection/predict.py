import pickle
from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()

def model_prediction(features):
    features = count_vec.transform([features]).toarray()
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Language Detection/model/Language_Detection_MultinomialNB.pkl', 'rb'))
    Language = str(list(pickled_model.predict(features)))
    
    return str(f'The Language is {Language}')


text = input('Enter your text')

print(model_prediction(text))

#This may throw error so please prefer the function inside the notebook.
