import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Online_payment_fraud_detection/model/Online_payment_fraud_detection_randomforest.pkl', 'rb'))
    isFraud = str(list(pickled_model.predict(features)))
    
    return str(f'The detection is {isFraud}')

step = int(input("Enter step"))
typeup = int(input("Enter type"))
amount = float(input("Enter amount"))
nameOrig = int(input("Enter name of orig"))
oldbalanceOrg = float(input("Enter old balance"))
newbalanceOrig = float(input("Enter new balance"))
nameDest = int(input("Enter new dest"))
oldbalanceDest = float(input("Enter old balanace dest"))
newbalanceDest = float(input("Enter new balance dest"))
isFlaggedFraud = int(input("Enter Fraud lagged or not"))

print(model_prediction([[step,typeup,amount,nameOrig,oldbalanceOrg,newbalanceOrig,nameDest,oldbalanceDest,newbalanceDest,isFlaggedFraud]]))