# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:26:59 2022

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/DELL/Desktop/machine learning/car price/random_forest.pkl','rb'))


def car_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
    print(prediction)
    
    
    return "selling price is", prediction
    
    
def main():
    
    st.title('Car Price Prediction App')

    
    Present_Price = st.text_input('Present_Price')
    
    Kms_Driven = st.text_input('Kms_Driven')
    
    Seller_Type = st.text_input('Seller_Type')
    
    Transmission = st.text_input('Transmission')
    
    Owner = st.text_input('Owner')
    
    no_of_years = st.text_input('no_of_years')
    
    Fuel_CNG = st.text_input('Fuel_CNG')
    
    Fuel_Diesel = st.text_input('Fuel_Diesel')
    
    Fuel_Petrol = st.text_input('Fuel_Petrol')
    
    
    
    diagonosis = " "
    
    if st.button('Car Prediction result'):
        
        diagonosis = car_prediction([Present_Price,Kms_Driven, Seller_Type,Transmission,Owner,no_of_years,Fuel_CNG,Fuel_Diesel,Fuel_Petrol])
        
        
        
    st.success(diagonosis)
    
    
if __name__ == '__main__':
    main()
    
    
    