# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:43:25 2022

@author: nikhil
"""

import pickle
import streamlit as st 

pickle_in = open('model355.pkl','rb')
model=pickle.load(pickle_in)

def predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity):
    
    prediction=model.predict([[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction

def main():
    st.title("Electrical Enegry Production of Combined Cycle Power Plant")
    html_temp="""
    </div>
    """
 
    st.markdown(html_temp,unsafe_allow_html=True)
    
    temperature =st.text_input("Temperature, in Degrees Celsius")
    exhaust_vacuum =st.text_input("Exhaust vacuum, in cm Hg")
    amb_pressure =st.text_input("Ambient pressure, in millibar")
    r_humidity =st.text_input("Relative Humidity, in percentage")
    result=""


    if st.button("Predict"):
        result=predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity)
        st.success('Electrical Energy Production of CCPP is {} in MW'.format(result))
        
        
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    