import pickle

def model_prediction(features):

     pickled_model = pickle.load(open('Microsoft_Stock_DTR.pkl', 'rb'))
     Stock_Price = str(list(pickled_model.predict(features)))

     return str(f'The Stock price is {Stock_Price}')

Open = float(input())
High = float(input())
Low = float(input())


print(model_prediction([[ Open, High, Low ]]))

