from model import Model
from train import Classifier
import pandas as pd
model= Model()
model.train_and_save()

cls = Classifier()
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
print(cls.load_and_test(new_claim))