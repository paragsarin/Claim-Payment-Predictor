from train import Classifier
import pandas as pd
pipeline = Classifier()

def test_response(requests, response):
    requests = pd.DataFrame({
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
    assert response == pipeline.load_and_test(requests)