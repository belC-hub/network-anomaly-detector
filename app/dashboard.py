# dashboard.py
# Streamlit dashboard for real-time anomaly detection

import streamlit as st
from src.main import run_pipeline
import pandas as pd

st.set_page_config(page_title="Network Anomaly Detector", layout="wide")
st.title("Network Anomaly Detection Dashboard")

# Sidebar: number of packets to capture
packet_count = st.sidebar.slider("Number of packets to capture", min_value=1, max_value=20, value=5)

# Capture & analyze packets
if st.button("Run Detection"):
    with st.spinner("Capturing and analyzing packets..."):
        results_df = run_pipeline(packet_count=packet_count)
        st.success("Detection complete!")

        # Show full table
        st.subheader("Captured Packets")
        st.dataframe(results_df)

        # Show anomalies only
        st.subheader("Anomalous Packets")
        anomalies = results_df[results_df['anomaly'] == -1]
        st.dataframe(anomalies)

        # Summary
        st.subheader("Summary")
        st.write(f"Total packets captured: {len(results_df)}")
        st.write(f"Total anomalies detected: {len(anomalies)}")
