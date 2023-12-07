# app.py
import streamlit as st
import joblib
import pandas as pd
import os



input_features = [
    'Date','Location','MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine',
    'WindGustDir','WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am',
    'WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am',
    'Cloud3pm','Temp9am','Temp3pm','RainToday'
]

# Se carga el pipeline del modelo.
path_dir=os.path.dirname(os.path.abspath(__file__))
pkl_path=os.path.join(path_dir, 'regresion_lineal_pipeline.pkl')
pipeReg = joblib.load(pkl_path)

pkl_path2=os.path.join(path_dir, 'regresion_logistica_pipeline.pkl')
pipeClass = joblib.load(pkl_path2)



st.title('Modelo de predicción Lluvias Australia')

def get_user_input():
    """
    This function generates the inputs for the Streamlit frontend so that the user can load the values.
    It also contains the button to submit and get the prediction.
    """
    input_dict = {}
    claves_out=['Date', 'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainTomorrow']

    with st.form(key='my_form'):
        # Add the new inputs
        categorical_features = ['Date', 'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']
        location_values = ['Sydney', 'SydneyAirport', 'Melbourne', 'MelbourneAirport', 'Canberra']
        wind_dir_values = ['SSW', 'E', 'ESE', 'W', 'ENE', 'S', 'SE', 'SSE', 'NE', 'NNE', 'NWW', 'NW', 'WWW', 'N', 'WSW', 'SW']
        rain_values = ['Yes', 'No']

        for feat in input_features:
            if feat in categorical_features:
                if feat == 'Location':
                    input_value = st.selectbox(f"Select value for {feat}", options=location_values)
                elif feat in ['WindGustDir', 'WindDir9am', 'WindDir3pm']:
                    input_value = st.selectbox(f"Select value for {feat}", options=wind_dir_values)
                elif feat == 'RainToday':
                    input_value = st.selectbox(f"Select value for {feat}", options=rain_values)
                    if input_value == "Yes": input_value = 1
                    else: input_value = 0
                else:
                    input_value = st.text_input(f"Enter value for {feat}")
            else:
                input_value = st.number_input(f"Enter value for {feat}", value=0.0, step=1.0)

            input_dict[feat] = input_value
        for clave in claves_out:
            if clave in input_dict:
                del input_dict[clave]
        submit_button = st.form_submit_button(label='Submit')

    return pd.DataFrame([input_dict]), submit_button


user_input, submit_button = get_user_input()


# When the 'Submit' button is pressed, perform the prediction
if submit_button:
    # Predict wine quality
    prediction = pipeClass.predict(user_input)
    prediction_value = 'Yes' if prediction[0] == 1 else 'No'

    prediction2 = pipeReg.predict(user_input)
    prediction_value2 = 0 if prediction2[0] < 0 else prediction2[0]


    # Display the prediction
    st.header("Llueve Mañana?")
    st.write(prediction_value)
    st.header("Cuanto Llueve?")
    st.write(prediction_value2)
