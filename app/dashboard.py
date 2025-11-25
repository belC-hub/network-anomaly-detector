# app/dashboard.py
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.main import run_pipeline

st.set_page_config(page_title="Network Anomaly Detector", layout="wide")
st.title("Network Anomaly Detector MVP")

st.markdown(
    """
    This dashboard captures dummy network packets and detects anomalies
    using multiple algorithms (simulated for testing).
    """
)

packet_count = st.sidebar.number_input(
    "Number of packets to capture",
    min_value=10,
    max_value=1000,
    value=100,
    step=10
)

if st.sidebar.button("Run Detection"):
    with st.spinner("Running anomaly detection..."):
        try:
            results_df = run_pipeline(packet_count=packet_count)
            st.success("Detection complete!")

            st.subheader("All Packets")
            st.dataframe(results_df)

            if 'is_anomaly' in results_df.columns:
                anomalies = results_df[results_df['is_anomaly'] == 1]
                st.subheader("Anomalous Packets Summary")
                st.write(f"Total anomalies detected: {len(anomalies)}")
                if len(anomalies) > 0:
                    st.dataframe(anomalies)
            else:
                st.warning("No 'is_anomaly' column found in results.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
