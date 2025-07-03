import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("bestmodel.pkl")

# Fungsi utama aplikasi
def run():
    st.title('Prediksi Employability Mahasiswa')
    st.header('Form Data Mahasiswa')

    with st.form('form_data'):
        cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, step=0.1)
        internships = st.selectbox('Jumlah Internship', options=[0, 1, 2, 3], index=0)
        projects = st.selectbox('Jumlah Project', options=[0, 1, 2, 3], index=0)
        certifications = st.selectbox('Jumlah Workshop/Certification', options=[0, 1, 2], index=0)
        aptitude = st.number_input('Aptitude Test Score', min_value=0.0, max_value=100.0, step=1.0)
        softskill = st.slider('Soft Skill Rating (1-5)', min_value=1.0, max_value=5.0, step=0.1)
        ssc = st.number_input('SSC Marks', min_value=0.0, max_value=100.0, step=0.5)
        hsc = st.number_input('HSC Marks', min_value=0.0, max_value=100.0, step=0.5)
        extracurricular = st.selectbox('Aktif dalam Ekstrakurikuler?', options=['No', 'Yes'], index=0)
        training = st.selectbox('Mengikuti Placement Training?', options=['No', 'Yes'], index=0)

        submit = st.form_submit_button('🔮 Prediksi')

    st.write('---')
    st.subheader('Data yang Dimasukkan')
    df = pd.DataFrame([{
        'CGPA': cgpa,
        'Internships': internships,
        'Projects': projects,
        'Workshops/Certifications': certifications,
        'AptitudeTestScore': aptitude,
        'SoftSkillsRating': softskill,
        'SSC_Marks': ssc,
        'HSC_Marks': hsc,
        'ExtracurricularActivities': extracurricular,
        'PlacementTraining': training
    }])

    st.dataframe(df)

    if submit:
        prediction = model.predict(df)[0]

        if prediction == 0:
            st.warning("⚠️ Mahasiswa diprediksi **TIDAK DITEMPATKAN**.")
        else:
            st.success("✅ Mahasiswa diprediksi **DITEMPATKAN**.")

if __name__ == '__main__':
    run()