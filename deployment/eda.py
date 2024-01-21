import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
def run ():
    # Create title
    st.title('Satisfaction Prediction')

    # Create sub-header
    st.subheader('Analysis Data for Employee Satisfaction')


    # Add Description
    st.write('This page made by **Betara Candra**')

    # Create Outline
    st.write('# This dataset is containing about data that can support predict employe satisfied. ')
    # Create markdowm line
    st.markdown('---')

    # Show dataframe
    df = pd.read_csv('https://raw.githubusercontent.com/betarac/dataset/main/Employee%20Satisfaction%20Index.csv')
    st.dataframe(df)
    st.write('')   
    # Visualisasi
    st.write('# Visualization')
    # Create Barplot
    st.write('## Distribution Age of Employee')
    fig = plt.figure(figsize=(12,5))
    ax = sns.countplot(df,x='age', hue='satisfied',)
    plt.title('Distribution age of employee')
    for i in ax.containers:
        ax.bar_label(i,)
    st.pyplot(fig)
    st.write('')  
    st.write('## Job level on employee satisfied') 
    # Plot for count of job level on satisfied
    fig2 = plt.figure(figsize=(12,5))
    ax = sns.countplot(data = df, x='job_level',hue='satisfied' )
    for i in ax.containers:
        ax.bar_label(i,)
    st.pyplot(fig)
    st.write('') 
    st.write('## Distribution of Education') 
    # Plot for count of job level on satisfied
    fig3,ax = plt.subplots(figsize=(6,4))
    df['education'].value_counts().plot(kind='pie', autopct='%.2f%%',ax=ax)
    plt.show()
    st.pyplot(fig3)
    st.write('') 

if __name__ == '__main__':
    run()