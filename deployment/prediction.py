import streamlit as st
import pickle 
import json 
import pandas as pd
import numpy as np

with open('model_pipeline_adabost.pkl', 'rb') as file_1: # To open model with best result, in this case the model is svm with parameter 
    pipeadabost = pickle.load(file_1)

def run() :
    # Create form 
    with st.form('form_satisfied') :
        id = st.text_input('Employee ID', value='', help='Player Name')
        age = st.number_input('Age', 
                            min_value = 23, max_value = 54, 
                            value=23,
                            step = 1,
                            help='Age')
        dept = st.radio('Departement',('HR', 'Technology', 'Sales', 
                                       'Purchasing', 'Marketing'),index=0)
        location = st.radio('Location',('Suburb', 'City'),index=0)
        edu = st.radio('Education',('PG','UG'),index=0)
        recruit = st.radio('Recruitment Type',
                           ('Referral', 'Walk-in', 
                            'On-Campus', 'Recruitment Agency'),index=0)
        st.write('---')
        job = st.slider('Job Level',1,5,1) # min,max,value
        rating = st.slider('Rating',1,5,1) # min,max,value
        onsite = st.slider('On Site',0,1,1) # min,max,value
        awards = st.slider('Awards',0,9,1) # min,max,value
        certif = st.slider('Certification',0,1,1) # min,max,value
        salary = st.radio('Salary',
                           (24076, 29805, 
                            42419, 65715,86750),index=0)
        st.write('---')
        submitted = st.form_submit_button('Predict')

        data_inf = {
            'emp_id':id, 
            'age':age,
            'Dept':dept,
            'location' : location,
            'education': edu,
            'recruitment_type' : recruit,
            'job_level': job,
            'rating':rating, 
            'onsite':onsite, 
            'awards':awards,
            'certifications':certif, 
            'salary':salary,
        }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Predict 
        y_inf_pred = pipeadabost.predict(data_inf)
        st.write('1 : Yes')
        st.write('0 : No')
        st.write('# Satisfied : ', str(int(y_inf_pred)) )

if __name__ == '__main__':
    run()