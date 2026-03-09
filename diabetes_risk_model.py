import os
from typing import Any, Dict, Optional, Tuple

import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(_file_))

# Final thresholds (kept here so backend + debug output agree)
THRESHOLD_A = 0.22
THRESHOLD_B = 0.50

_stageA_model: Optional[Any] = None
_stageB_model: Optional[Any] = None
_features: Optional[Any] = None


def _load_artifacts() -> Tuple[Any, Any, Any]:
    """
    Lazily load model artifacts so importing the app doesn't crash when
    .pkl files aren't present (common in repos / fresh deployments).
    """
    global _stageA_model, _stageB_model, _features

    if _stageA_model is None:
        _stageA_model = joblib.load(os.path.join(BASE_DIR, "stageA_model.pkl"))
    if _stageB_model is None:
        _stageB_model = joblib.load(os.path.join(BASE_DIR, "stageB_model.pkl"))
    if _features is None:
        _features = joblib.load(os.path.join(BASE_DIR, "feature_list.pkl"))

    return _stageA_model, _stageB_model, _features


def predict_with_scores(input_df: pd.DataFrame) -> Dict[str, Any]:
    """
    input_df: DataFrame with same columns as training data
    returns:
        class_id: 0=Normal, 1=Prediabetes, 2=Diabetes
        stageA_prob: probability from stage A (positive class)
        stageB_prob: probability from stage B (positive class) if stage A passed else None
        risk_prob: probability used to compute risk_score
    """
    stageA_model, stageB_model, features = _load_artifacts()

    input_df = input_df[features]

    probA = stageA_model.predict_proba(input_df)[:, 1]
    stageA_prob = float(probA[0])

    if stageA_prob < THRESHOLD_A:
        return {
            "class_id": 0,
            "stageA_prob": stageA_prob,
            "stageB_prob": None,
            "risk_prob": stageA_prob,
        }

    probB = stageB_model.predict_proba(input_df)[:, 1]
    stageB_prob = float(probB[0])

    return {
        "class_id": 2 if stageB_prob >= THRESHOLD_B else 1,
        "stageA_prob": stageA_prob,
        "stageB_prob": stageB_prob,
        "risk_prob": stageB_prob,
    }


def final_predict(input_df: pd.DataFrame) -> int:
    return int(predict_with_scores(input_df)["class_id"])
