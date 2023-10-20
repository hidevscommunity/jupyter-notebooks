import pickle


def model_prediction(features):
    pickled_model = pickle.load(open('breast_cancer_Logistic_Regression.pkl', 'rb'))
    Patient = str(list(pickled_model.predict(features)))

    return str(f'The Patient is {Patient}')


Age = float(input())
Gender = int(input())
Protein1 = float(input())
Protein2 = float(input())
Protein3 = float(input())

Protein4 = float(input())
Tumour_Stage = int(input())

Histology = int(input())
HER2_status = int(input())
Surgery_type = int(input())





print(model_prediction([[ Age, Gender, Protein1, Protein2,
                          Protein3, Protein4, Tumour_Stage,
                          Histology, HER2_status, Surgery_type]]))