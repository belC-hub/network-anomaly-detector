# capture.py
# MVP-friendly packet capture (simulated)

def capture_packets(count=5):
    """
    Return a list of fake packets for testing.
    Each packet has 'src', 'dst', and 'len' keys.
    """
    packets_list = []
    for i in range(count):
        packets_list.append({
            "src": f"192.168.0.{i+1}",
            "dst": "192.168.0.100",
            "len": 60 + i*10
        })
    return packets_list
