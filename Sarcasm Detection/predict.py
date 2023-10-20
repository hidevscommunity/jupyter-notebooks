import pickle
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()


def model_prediction(features):
    features = cv.transform([features]).toarray()
    pickled_model = pickle.load(open('Sarcasm_Detection_BernoulliNB.pkl', 'rb'))
    Message = str(list(pickled_model.predict(features)))

    return str(f'The Message is {Message}')

message = input('Enter your comment')


print(model_prediction(message))


# This may throw error so please prefer the function inside the notebook.