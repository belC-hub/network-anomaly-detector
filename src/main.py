# src/main.py
import pandas as pd
from src.capture import capture_packets
from src.preprocess import packets_to_dataframe
from src.detectors import run_isolation_forest, run_one_class_svm

def run_pipeline(packet_count=100):
    """
    Captures packets, converts to DataFrame, runs anomaly detectors.
    Returns DataFrame with 'is_anomaly' column.
    """
    packets = capture_packets(packet_count)
    df = packets_to_dataframe(packets)

    # Run detectors
    predictions = pd.DataFrame(index=df.index)
    predictions['iforest'] = run_isolation_forest(df)
    predictions['ocsvm'] = run_one_class_svm(df)

    # Combine with majority vote
    df['is_anomaly'] = predictions.mean(axis=1).apply(lambda x: 1 if x >= 0.5 else 0)

    return df
