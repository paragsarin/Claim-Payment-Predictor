import requests
import streamlit as st
from train import Classifier
import math
import numpy as np
import pandas as pd
def predict_class_local(age,ICD10,work):
    #dt = list(map(sepl))
    #S00.01XA", "S00.01XD", "S41.0","S41.1"
    #["Active", "Heavy", "Light","Sedentary"],
    a=0
    b=0
    c=0
    d=0
    w1=0
    w2=0
    w3=0
    w4=0
    if ICD10 == 'S00.01XA':
        a=1
    elif ICD10 == 'S00.01XD':
        b=1
    elif ICD10 == 'S41.0':
        c=1
    elif ICD10 == 'S41.1':
        d=1
    
    if work == 'Active':
        w1=1
    elif work == 'Heavy':
        w2=1
    elif work == 'Light':
        w3=1
    elif work == 'Sedentary':
        w4=1

    req = {
            'Age': [age],
            'ICD10_codes_S00.01XA': [a],          # Use the same column names as in the training data
            'ICD10_codes_S00.01XD': [b],
            'ICD10_codes_S41.0': [c],
            'ICD10_codes_S41.1': [d],
            'Type_of_Work_Active': [w1],
            'Type_of_Work_Heavy Work': [w2],
            'Type_of_Work_Light Active': [w3],
            'Type_of_Work_Sedentary':[w4]
         }
    new_claim = pd.DataFrame({
           'Age': [age],
            'ICD10_codes_S00.01XA': [a],          # Use the same column names as in the training data
            'ICD10_codes_S00.01XD': [b],
            'ICD10_codes_S41.0': [c],
            'ICD10_codes_S41.1': [d],
            'Type_of_Work_Active': [w1],
            'Type_of_Work_Heavy Work': [w2],
            'Type_of_Work_Light Active': [w3],
            'Type_of_Work_Sedentary':[w4]
        
        })
    print(new_claim)
    cls = Classifier()
    return cls.load_and_test(new_claim)

def predict_class_aws(sepl, sepw, petl, petw):
    API_URL = "https://ti53furxkb.execute-api.us-east-1.amazonaws.com/test/classify"

    dt = list(map(float,[sepl, sepw, petl, petw]))

    req = {
        "data": [
            dt
        ]
    }

    r = requests.post(API_URL, json=req)
    return r.json()

### Streamlit code (works as a straigtht-forward script) ###
st.title("Welcome to Claims Predictor")
st.header("Predict Claims Payment")

age = int(st.text_input('Age:',"0"))
ICD10=st.radio(
    "Please Select ICD10 Code:",
    ["S00.01XA", "S00.01XD", "S41.0","S41.1"],
    index=None,
)
work=st.radio(
    "Please Select work Type:",
    ["Active", "Heavy", "Light","Sedentary"],
    index=None,
)


left, right = st.columns(2)
with left:
    if st.button("Predict"):
        ret = predict_class_local(age,ICD10,work)
       
        st.write(f"***Prediction:*** {ret['prediction']}")
   

#with right:
    #if st.button("Predict AWS"):
     #   ret = predict_class_aws(age)
       
      #  st.write(f"Prediction: {ret['prediction'][0]}")
      