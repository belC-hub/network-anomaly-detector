# src/detectors.py
import pandas as pd
import numpy as np

def run_isolation_forest(df: pd.DataFrame) -> pd.Series:
    """
    Dummy Isolation Forest stub.
    Returns random 0/1 as anomalies.
    """
    np.random.seed(42)
    return pd.Series(np.random.choice([0, 1], size=len(df)), index=df.index)

def run_one_class_svm(df: pd.DataFrame) -> pd.Series:
    """
    Dummy One-Class SVM stub.
    Returns random 0/1 as anomalies.
    """
    np.random.seed(24)
    return pd.Series(np.random.choice([0, 1], size=len(df)), index=df.index)
