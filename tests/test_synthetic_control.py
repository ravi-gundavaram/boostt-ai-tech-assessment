import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from synthetic_control import build_synthetic_control

import pandas as pd
from synthetic_control import build_synthetic_control

def test_synthetic_control_basic():
    df = pd.DataFrame({
        "geo": ["A", "B", "C", "T"],
        "pre_spend": [100, 120, 110, 105],
        "post_spend": [115, 125, 118, 0],  # 0 is placeholder for treated
    })
    predicted = build_synthetic_control(df, treated_geo="T", predictors=["pre_spend"])
    assert isinstance(predicted, float)
    assert predicted > 0
