import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    return joblib.load('rf_employees_model.pkl')


st.title("Performance Rating Prediction App")
st.write("This app helps INX Future Inc to predict the employee performance based on input factors. This will be used to hire employees ")

model = load_model()

# Define the selected 10 features
selected_features = [
    'EmpEnvironmentSatisfaction', 'EmpLastSalaryHikePercent',
    'YearsSinceLastPromotion', 'EmpJobRole', 'ExperienceYearsInCurrentRole',
    'EmpDepartment', 'EmpHourlyRate', 'ExperienceYearsAtThisCompany', 'Age',
    'EmpWorkLifeBalance'
]

# User Inputs
EmpEnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
EmpLastSalaryHikePercent = st.number_input("Last Salary Hike Percent", min_value=0, step=1)
YearsSinceLastPromotion = st.number_input("Years Since Last Promotion", min_value=0, step=1)
EmpJobRole = st.selectbox("Job Role", ["Business Analyst", "Data Scientist", "Delivery Manager", "Developer", "Finance Manager", "Healthcare Representative", "Human Resources", "Laboratory Technician", "Manager", "Manager R&D", "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative", "Senior Developer", "Senior Manager R&D", "Technical Architect", "Technical Lead"])
ExperienceYearsInCurrentRole = st.number_input("Experience in Current Role (Years)", min_value=0, step=1)
EmpDepartment = st.selectbox("Department", ["Sales", "Research and Development", "Human Resource", "Finance", "Data Science", "Development"])
EmpHourlyRate = st.number_input("Hourly Rate", min_value=30, step=1)
ExperienceYearsAtThisCompany = st.number_input("Experience at Company (Years)", min_value=0, step=1)
Age = st.number_input("Age", min_value=18, max_value=60, step=1)
EmpWorkLifeBalance = st.selectbox("Work-Life Balance", [1, 2, 3, 4])


# Encode categorical variables
job_role_mapping = {role: i for i, role in enumerate([
    "Business Analyst", "Data Scientist", "Delivery Manager", "Developer", 
    "Finance Manager", "Healthcare Representative", "Human Resources", "Laboratory Technician", 
    "Manager", "Manager R&D", "Manufacturing Director", "Research Director", 
    "Research Scientist", "Sales Executive", "Sales Representative", 
    "Senior Developer", "Senior Manager R&D", "Technical Architect", "Technical Lead"
])}
department_mapping = {dept: i for i, dept in enumerate([
    "Sales", "Research and Development", "Human Resource", "Finance", "Data Science", "Development"
])}

# Convert selected values to numerical form
EmpJobRole = job_role_mapping[EmpJobRole]
EmpDepartment = department_mapping[EmpDepartment]


# Predict Price
if st.button("Predict Performance Rating"):
    input_data = np.array([[EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, YearsSinceLastPromotion, EmpJobRole, ExperienceYearsInCurrentRole,
    EmpDepartment, EmpHourlyRate, ExperienceYearsAtThisCompany, Age, EmpWorkLifeBalance]])
    prediction = model.predict(input_data)
    if prediction[0] == 4:
        predicted_label = "Outstanding"
    elif prediction[0] == 3:
        predicted_label = "Excellent"
    else:
        predicted_label = "Good"

    st.subheader(f"Prediction of Perfomance Rating: {predicted_label}")
 