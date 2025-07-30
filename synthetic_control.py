import pandas as pd
from sklearn.linear_model import RidgeCV

def build_synthetic_control(df: pd.DataFrame, treated_geo: str, predictors: list) -> float:
    df_control = df[df["geo"] != treated_geo]
    df_treated = df[df["geo"] == treated_geo]

    X_train = df_control[predictors]
    y_train = df_control["post_spend"]

    model = RidgeCV(alphas=[0.1, 1.0, 10.0])
    model.fit(X_train, y_train)

    X_test = df_treated[predictors]
    predicted = model.predict(X_test)

    return predicted.mean()  # Estimated counterfactual post_spend
