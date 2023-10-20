import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Amazon Recommendation/model/Amazon_Recommendation_LinearRegression.pkl', 'rb'))
    ID = str(list(pickled_model.predict(features)))
    
    return str(f'The Product ID is {ID}')

score = int(input("Enter the score of the product: -"))
Rank =  int(input("Enter the Rank of the product: -"))   

print(model_prediction([[score,Rank]]))