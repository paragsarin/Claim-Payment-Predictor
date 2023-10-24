import numpy as np
from scipy.sparse.construct import spdiags
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib
import pickle

class Model:
    def __init__(self):
        pass

    @staticmethod
    def train_and_save():
        data = pd.read_csv('claim_payment_dataset.csv')

    # One-hot encode the categorical features
        data = pd.get_dummies(data, columns=['ICD10_codes', 'Type_of_Work'])

        # Define features and target
        X = data.drop('Total_Claim_Payment', axis=1)
        y = data['Total_Claim_Payment']

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        print(X_train.head())
        print(y_train)
        # Initialize and train the linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        pickle.dump(model, open("model.pkl", "wb"))