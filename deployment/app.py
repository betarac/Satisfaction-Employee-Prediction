import pandas as pd 
import streamlit as st
import eda 
import prediction
from PIL import Image
page = st.sidebar.selectbox('Choose Pages: ' , 
                            ('Landing Page','Data Exploration','Data Prediction'))
if page == 'Landing Page':
    st.title('*Satisfaction Prediction*')
    st.write('')
    st.write('# Name      : Betara Candra')
    st.write('# Batch     : SBY - 002')
    st.write('# Objective : To Predict that employee satisfaction or not')
    st.write('## Please select menu on left bar')
    image = Image.open('employe.jfif')
    st.image(image,caption="Employee")
elif page == 'Data Exploration' :
    eda.run()
else:
    prediction.run()