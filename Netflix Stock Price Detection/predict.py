import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/My Sample Notebook/Notebook Template/Netflix Stock Price Detection/model/Netflix_Stock_DecisionTree.pkl', 'rb'))
    Stock_Price = str(list(pickled_model.predict(features)))
    
    return str(f'The Stock price of Netflix is {Stock_Price}')

Open = float(input("Enter the Open value"))
High = float(input("Enter the High value"))
Low = float(input("Enter the Low value"))


print(model_prediction([[ Open, High, Low ]]))



