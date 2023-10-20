import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('Model\Employee_Attrition_ra.pkl', 'rb'))
    TravelInsurance = str(pickled_model.predict(features)[0])
    if TravelInsurance=='1':
        TravelInsurance='Yes'
    else:
        TravelInsurance='No'
    
    return str(f'The Employee Attrition is {TravelInsurance}')

Age = int(input())
BusinessTravel = int(input())
DailyRate = int(input())
Department = int(input())
DistanceFromHome = int(input())
Education = int(input())
EducationField = int(input())
EmployeeCount = int(input())
EmployeeNumber = int(input())
EnvironmentSatisfaction = int(input())
Gender = int(input())
HourlyRate = int(input())
JobInvolvement = int(input())
JobLevel = int(input())
JobRole = int(input())
JobSatisfaction = int(input())
MaritalStatus = int(input())
MonthlyIncome = int(input())
MonthlyRate = int(input())
NumCompaniesWorked = int(input())
Over18 = int(input())
OverTime = int(input())
PercentSalaryHike = int(input())
PerformanceRating = int(input())
RelationshipSatisfaction = int(input())
StandardHours = int(input())
StockOptionLevel = int(input())
TotalWorkingYears = int(input())
TrainingTimesLastYear = int(input())
WorkLifeBalance = int(input())
YearsAtCompany = int(input())
YearsInCurrentRole = int(input())
YearsSinceLastPromotion = int(input())
YearsWithCurrManager = int(input())

print(model_prediction([[Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager]]))