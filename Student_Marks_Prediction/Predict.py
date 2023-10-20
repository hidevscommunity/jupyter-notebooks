import pickle

def prediction(features):
    
    pickled_model = pickle.load(open('Student_Marks_LinearRegresssionnew.pkl', 'rb'))
    Stmarks = str(list(pickled_model.predict(features)))
    
    return str(f'The Student Marks is {Stmarks}')

number_courses = int(input())
time_study = int(input())
print(prediction([[number_courses,time_study]]))