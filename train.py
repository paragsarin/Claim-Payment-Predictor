import pickle
from model import Model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib
import pickle


class Classifier:
    def __init__(self):
        print("aa")
        pass

    def train(self):
        print("hello")
        model = Model()
        model.train_and_save()

    def load_and_test(self, req):
        print("bb")
        model = pickle.load(open("model.pkl", "rb"))
        
        new_claim = pd.DataFrame({
            'Age': [40],
            'ICD10_codes_S00.01XA': [0],          # Use the same column names as in the training data
            'ICD10_codes_S00.01XD': [1],
            'ICD10_codes_S41.0': [0],
            'ICD10_codes_S41.1': [0],
            'Type_of_Work_Active': [1],
            'Type_of_Work_Heavy Work': [0],
            'Type_of_Work_Light Active': [0],
            'Type_of_Work_Sedentary':[0]
        
        })
        print("cc")

        print(req)


        # Predict the total claim payment for the new claim
        predicted_claim_payment = model.predict(req)

        return {"prediction": predicted_claim_payment[0]}