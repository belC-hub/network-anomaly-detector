# main.py
# Ties everything together: capture, preprocess, detect, judge

from src.capture import capture_packets
from src.preprocess import packets_to_dataframe
from src.detectors import AnomalyDetectors
from src.judge import majority_vote

def run_pipeline(packet_count=10):
    # Step 1: Capture packets
    packets = capture_packets(count=packet_count)
    print(f"Captured {len(packets)} packets")

    # Step 2: Preprocess packets
    df = packets_to_dataframe(packets)
    print("Preprocessed data:")
    print(df)

    # Step 3: Train anomaly detectors
    detectors = AnomalyDetectors()
    detectors.fit(df)
    predictions = detectors.predict(df)

    # Step 4: Get final decision
    final = majority_vote(predictions)
    df['anomaly'] = final
    print("Final results:")
    print(df)

    return df

# Run the pipeline if executed directly
if __name__ == "__main__":
    run_pipeline(packet_count=5)
