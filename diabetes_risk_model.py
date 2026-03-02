import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained models
stageA_model = joblib.load(os.path.join(BASE_DIR, "stageA_model.pkl"))
stageB_model = joblib.load(os.path.join(BASE_DIR, "stageB_model.pkl"))
FEATURES = joblib.load(os.path.join(BASE_DIR, "feature_list.pkl"))

# Final thresholds
THRESHOLD_A = 0.22
THRESHOLD_B = 0.50

def final_predict(input_df):
    """
    input_df: DataFrame with same columns as training data
    returns:
        0 = Normal
        1 = Prediabetes
        2 = Diabetes
    """

    input_df = input_df[FEATURES]

    probA = stageA_model.predict_proba(input_df)[:, 1]

    if probA[0] < THRESHOLD_A:
        return 0

    probB = stageB_model.predict_proba(input_df)[:, 1]
    return 2 if probB[0] >= THRESHOLD_B else 1
