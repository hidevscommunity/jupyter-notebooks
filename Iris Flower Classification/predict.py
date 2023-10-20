import pickle

def model_prediction(features):    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Iris_Flower_Classification/model/Iris_Flower_Classification_RandomForest.pkl', 'rb'))
    variety = str(list(pickled_model.predict(features)))
    
    return str(f'The species is {variety}')

sepal_length = float(input("Enter the sepal length"))
sepal_width = float(input("Enter the sepal width"))
petal_length = float(input("Enter the petal length"))
petal_width = float(input("Enter the petal width"))

print(model_prediction([[sepal_length,sepal_width,petal_length,petal_width]]))