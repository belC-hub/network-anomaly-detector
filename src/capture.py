# src/capture.py
import pandas as pd

def capture_packets(packet_count=100):
    """
    Dummy packet capture.
    Returns a list of dicts representing network packets.
    """
    packets = []
    for i in range(packet_count):
        packets.append({
            "src": f"192.168.0.{i%255}",
            "dst": f"10.0.0.{i%255}",
            "length": i % 1500,
            "protocol": "TCP" if i % 2 == 0 else "UDP"
        })
    return packets
