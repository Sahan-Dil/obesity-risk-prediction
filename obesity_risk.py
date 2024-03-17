# --Sahan Dilshan--
# --11.03.2024--

import numpy as np
import pickle
import streamlit as st
import xgboost

#load the saved model - read binary
loaded_model = pickle.load(open('obesityriskapp.pkl', 'rb'))

#create function for prediction
def prediction(input_data):

    obesity_types = {
    0: "Underweight",
    1: "Normal weight",
    2: "Overweight",
    3: "Obesity Type I",
    4: "Obesity Type II",
    5: "Obesity Type III"
    }
    
    # Make prediction
    predicted_value = loaded_model.predict(input_data)
    res = obesity_types[int(predicted_value)]
    return res

def validation():
    return

def main():

    #Title
    st.title('obesity risk prediction app')

    #get input
    age = st.slider('Select Age', min_value=0, max_value=100, value=30, step=1)

    FCVC = st.number_input('Frequenly consumpting of vegetables (FCVC)', value=1.5000, step=0.1)

    NCP = st.number_input('Number of main meals (NCP)', value=3, step=1)

    CH2O = st.number_input('Consumption of water daily (CH20)', value=2, step=1)

    FAF = st.number_input('Physical activity frequency (FAF)', value=1.5000, step=0.1)

    TUE = st.number_input('Time using technology devices (TUE)', value=2, step=1)

    gender_options = ['Male', 'Female']
    gender = st.selectbox('Gender', options=gender_options)

    family_history_with_overweight = st.selectbox('Family history with overweight', options=['No', 'Yes'])

    FAVC_options = ['Yes', 'No']
    FAVC = st.selectbox('Frequent consumption of high caloric food (FAVC)', options=FAVC_options)

    CAEC_options = ['Always', 'Frequently', 'Sometimes', 'No']
    CAEC = st.selectbox('Consumption of food between meals (CAEC)', options=CAEC_options)

    SMOKE = st.selectbox('Smoke?', options=['No', 'Yes'])

    SCC_options = ['Yes', 'No']
    SCC = st.selectbox('Calories consumption monitoring (SCC)', options=SCC_options)

    CALC_options = ['Frequently', 'Sometimes', 'No']
    CALC = st.selectbox('Consumption of alcohol (CALC)', options=CALC_options)

    MTRANS_options = ['Automobile', 'Motorbike', 'Bike', 'Public_Transportation', 'Walking']
    MTRANS = st.selectbox('Transportation used (MTRANS)', options=MTRANS_options)

    height = st.number_input('Height (cm)', value=170, step=1)

    weight = st.number_input('Weight (kg)', value=70, step=1)
    
    # predictions
    res = ''

    if st.button('Predict'):

        FAVC_encoded = 1 if FAVC == 'Yes' else 0

        Gender_Female = 1 if gender == 'Female' else 0
        Gender_Male = 1 if gender == 'Male' else 0

        family_history_with_overweight_no = 1 if family_history_with_overweight == 'No' else 0
        family_history_with_overweight_yes = 1 if family_history_with_overweight == 'Yes' else 0

        FAVC_no = 1 if FCVC == 'No' else 0
        FAVC_yes = 1 if FCVC == 'Yes' else 0

        CAEC_Always = 1 if CAEC == 'Always' else 0
        CAEC_Frequently = 1 if CAEC == 'Frequently' else 0
        CAEC_Sometimes = 1 if CAEC == 'Sometimes' else 0
        CAEC_no = 1 if CAEC == 'No' else 0

        SMOKE_no = 1 if SMOKE == 'No' else 0
        SMOKE_yes = 1 if SMOKE == 'Yes' else 0

        SCC_no = 1 if SCC == 'No' else 0
        SCC_yes = 1 if SCC == 'Yes' else 0

        CALC_Frequently = 1 if CALC == 'Frequently' else 0
        CALC_Sometimes = 1 if CALC == 'Sometimes' else 0
        CALC_no = 1 if CALC == 'No' else 0

        MTRANS_Automobile = 1 if MTRANS == 'Automobile' else 0
        MTRANS_Bike = 1 if MTRANS == 'Bike' else 0
        MTRANS_Motorbike = 1 if MTRANS == 'Motorbike' else 0
        MTRANS_Public_Transportation = 1 if MTRANS == 'Public_Transportation' else 0
        MTRANS_Walking = 1 if MTRANS == 'Walking' else 0

        BMI = weight / ((height / 100) ** 2)
        print('BMI:::', BMI)

        input_data = ([[age, FAVC_encoded, NCP, CH2O, FAF, TUE, Gender_Female, Gender_Male, family_history_with_overweight_no, family_history_with_overweight_yes,
                        FAVC_no, FAVC_yes, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, SMOKE_no, SMOKE_yes, SCC_no, SCC_yes, CALC_Frequently,
                        CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking, BMI]])
        
       
        input_data_array = (input_data)

    #     ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE', 'Gender_Female',
    #    'Gender_Male', 'family_history_with_overweight_no',
    #    'family_history_with_overweight_yes', 'FAVC_no', 'FAVC_yes',
    #    'CAEC_Always', 'CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no',
    #    'SMOKE_no', 'SMOKE_yes', 'SCC_no', 'SCC_yes', 'CALC_Frequently',
    #    'CALC_Sometimes', 'CALC_no', 'MTRANS_Automobile', 'MTRANS_Bike',
    #    'MTRANS_Motorbike', 'MTRANS_Public_Transportation', 'MTRANS_Walking',
    #    'BMI']
  
        
        # Call prediction function
        res = prediction(input_data_array)

        if res == 'Normal weight':
            st.success(res)   
        else:
            st.error("Warning! Your are in :  {}.".format(res))

if __name__ == '__main__':
    main()
    

