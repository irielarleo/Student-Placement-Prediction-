import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Iriel Aureleo')
    st.write('Batch     : HCK-027')
    st.write('Tujuan Milestone    : ')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('lorem ipsum')

    with st.expander("Problem Statement"):
            st.caption('lorem ipsum')

    with st.expander("Kesimpulan"):
        st.caption('lorem ipsum')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     models .run()