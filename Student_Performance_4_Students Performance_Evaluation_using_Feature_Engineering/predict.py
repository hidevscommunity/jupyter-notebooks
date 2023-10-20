import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Student_Performance_4_Students Performance_Evaluation_using_Feature_Engineering/model/Students_Performance_Prediction_linear.pkl', 'rb'))
    score_mean = str(list(pickled_model.predict(features)))
    
    return str(f'The amount of the tip is {score_mean}')

gender = int(input("Enter Gender"))
race_ethnicity = int(input("Enter race"))
parental_level_of_education = int(input("Enter parental level of education"))
lunch = int(input("Enter lunch"))
test_preparation_course = int(input("Enter test prepration course"))
math_score = int(input("Enter math score"))
reading_score = int(input("Enter reading score"))
writing_score = float(input("Enter writing score"))

print(model_prediction([[gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score]]))