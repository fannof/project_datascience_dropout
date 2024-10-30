import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Course, encoder_Fathers_occupation, encoder_International, encoder_Mothers_occupation, encoder_Scholarship_holder
from prediction import prediction

st.set_page_config(page_title="Student Performance Prediction App", layout="wide")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .reportview-container {
        padding: 10px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #4b7bec;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True
)

col1, col2 = st.columns([1, 6])
with col1:
    st.image("image/logo.png", width=120)
with col2:
    st.title("🎓 Students Performance Prediction App")
    st.write("A prototype application to predict the academic status of students based on various attributes.")

st.markdown("## 📊 Input Student Data")

data = pd.DataFrame()

with st.form("student_data_form"):
    st.markdown("### Personal Information")

    col1, col2, col3= st.columns(3)

    with col1:
        Application_order = int(st.number_input(label='Application Order', value=1))
        data["Application_order"] = [Application_order]

    with col2:
        Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=1)
        data["Course"] = [Course]
        
    with col3:
        Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade', value=160.0))
        data["Previous_qualification_grade"] = [Previous_qualification_grade]

    col1, col2, col3= st.columns(3)
    with col1:
        Mothers_occupation = st.selectbox(label='Mothers Occupation', options=encoder_Mothers_occupation.classes_, index=1)
        data["Mothers_occupation"] = [Mothers_occupation]

    with col2:
        Fathers_occupation = st.selectbox(label='Fathers Occupation', options=encoder_Fathers_occupation.classes_, index=1)
        data["Fathers_occupation"] = [Fathers_occupation]

    with col3:
        Admission_grade = float(st.number_input(label='Admission Grade', value=160.0))
        data["Admission_grade"] = [Admission_grade]

    st.markdown("### Academic Performance")
    col1, col2, col3= st.columns(3)
    with col1:
        Scholarship_holder = st.selectbox(label='Scholarship Holder', options=encoder_Scholarship_holder.classes_, index=1)
        data["Scholarship_holder"] = [Scholarship_holder]

    with col2:
        International = st.selectbox(label='International', options=encoder_International.classes_, index=1)
        data["International"] = [International]

    with col3:
        Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular Units 1st Sem Credited', value=4))
        data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]

    col1, col2, col3= st.columns(3)
    with col1:
        Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular Units 1st Sem Enrolled', value=8))
        data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]

    with col2:
        Curricular_units_1st_sem_evaluations = float(st.number_input(label='Curricular Units 1st Sem Evaluation', value=14))
        data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]

    with col3:
        Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular Units 1st Sem Approved', value=1))
        data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]

    col1, col2, col3= st.columns(3)
    with col1:
        Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular Units 1st Sem Grade', value=14.94444))
        data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]

    with col2:
        Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular Units 2nd Sem Credited', value=4))
        data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]

    with col3:
        Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular Units 2nd Sem Enrolled', value=8))
        data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

    col1, col2= st.columns(2)
    with col1:
        Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular units 2nd Sem Evaluation', value=1))
        data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]

    with col2:
        Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular Units 2nd Sem Approved', value=4))
        data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

    col1, col2= st.columns(2)
    with col1:
        Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular Units 2nd Sem Grade', value=14.3456698))
        data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

    with col2:
        GDP = float(st.number_input(label='GDP', value=1.68))
        data["GDP"] = [GDP]

    submitted = st.form_submit_button(label="🔍 Predict Student Status")

if submitted:
    st.markdown("## 🔮 Prediction Results")
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(new_data)

    prediction_result = prediction(new_data)
    st.success(f"**Prediction: {prediction_result}**")

    st.download_button(label="📥 Download Data", data=new_data.to_csv(), file_name="processed_student_data.csv", mime="text/csv")

with st.expander("View Raw Input Data"):
    st.dataframe(data)