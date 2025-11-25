# Network Anomaly Detector MVP

A simple and accessible **Network Anomaly Detection** dashboard built with Python and Streamlit.  
This MVP captures network packets (simulated for testing purposes), preprocesses them, and detects anomalies using multiple machine learning algorithms with a majority vote approach.

**Live Demo:** [Streamlit App](https://network-anomaly-detector-eoq3ghtwqvww2jgfawabnj.streamlit.app/)

## Features

- Capture a user-defined number of network packets (simulated).
- Detect anomalies using multiple algorithms (Isolation Forest, One-Class SVM – dummy implementations for MVP).
- Visual dashboard with:
  - Table of all packets
  - Summary of anomalous packets
- Fully testable locally and on Streamlit Cloud.

## Installation & Running Locally

1. **Clone the repository**

```bash
git clone https://github.com/belC-hub/network-anomaly-detector.git
cd network-anomaly-detector2
