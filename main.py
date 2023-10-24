from train import Classifier
import pandas as pd
cls = Classifier()

def lambda_handler(event, context):
    try:
        new_claim =pd.DataFrame(event)
        return cls.load_and_test(new_claim)
    except Exception as e:
        raise
