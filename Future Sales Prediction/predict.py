import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('future_sales_pred_li.pkl', 'rb'))
    sold = str(pickled_model.predict(features)[0][0])
    
    return str(f'The number of units sold is {sold}')

TV=float(input("Enter the cost spent for advertising on TV: - "))
Radio=float(input("Enter the cost spent for advertising on Radio: - "))
Newspaper=float(input("Enter the cost spent for advertising on Newspaper: - "))

print(model_prediction([[TV, Radio, Newspaper]]))