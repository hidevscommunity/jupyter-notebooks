import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Order_Cancellation_Prediction/model/Order_Cancellation_Prediction_Logistic.pkl', 'rb'))
    cancelledOrNoShow = str(list(pickled_model.predict(features)))
    
    return str(f'The order cancellation is {cancelledOrNoShow}')

roomCount = int(input("Enter roomcount"))
is_cardless = int(input("Enter cardless or not"))
stars = float(input("Enter stars"))
NormalizedTotalBookingPrice = int(input("Enter Normalized total booking price"))
NormalizedLowRate = int(input("Enter rate"))
numberOfBookedNights = int(input("Enter number of booked nights"))
numberOfReviews = int(input("Enter review"))
AvgUserRating = float(input("Enter average rating"))
hasSpecialRequest = int(input("Enter any request"))
hasFreeCancellation = int(input("Enter having free cancellation"))

print(model_prediction([[roomCount,is_cardless,stars,NormalizedTotalBookingPrice,NormalizedLowRate,numberOfBookedNights,numberOfReviews,AvgUserRating,hasSpecialRequest,hasFreeCancellation]]))