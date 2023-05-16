import streamlit as st
import numpy as np
import pandas as pd
import joblib
import sklearn

model = joblib.load(r'model/rf_final.joblib')


st.set_page_config(page_title='Wild Blueberry Yield Prediction',layout='wide')

st.markdown("<h1 style= 'text-align: center;'>Wild Blueberry Yield Prediction application </h1",unsafe_allow_html=True)

def main():

    with st.form('prediction_form'):
        clonesize = st.slider('Clone Size: ',10.0,40.0,format="%d")
        honeybee = st.number_input(label='Honeybee',step=0.01,format='%.2f')
        bumbles = st.number_input(label='Bumbles',step=0.01,format='%.2f')
        osmia = st.number_input(label='Osmia',step=0.01,format='%.2f')
        avg_upper_temp = st.number_input(label='Average Upper Temperature',step=0.01,format='%.2f')
        avg_lower_temp = st.number_input(label='Average Lower Temperature',step=0.01,format='%.2f')
        avg_raining_days = st.number_input(label='Average Raining Days',step=0.01,format='%.2f')


        data = [[clonesize,honeybee,bumbles,osmia,avg_upper_temp,avg_lower_temp,avg_raining_days]]
       

        submit = st.form_submit_button('Predict')

    if submit:

        prediction = model.predict(data)[0]
        st.write(f'Blueberry yield is {prediction}')

if __name__ == '__main__':
    main()