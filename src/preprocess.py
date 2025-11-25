# preprocess.py
# Responsible for converting captured packets into features

import pandas as pd

def packets_to_dataframe(packets):
    """
    Convert a list of packet dictionaries into a pandas DataFrame.
    """
    df = pd.DataFrame(packets)

    # Simple preprocessing: encode IPs as integers
    df['src'] = df['src'].apply(lambda x: sum([int(i) for i in x.split('.')]))
    df['dst'] = df['dst'].apply(lambda x: sum([int(i) for i in x.split('.')]))
    
    return df

# Test preprocessing
if __name__ == "__main__":
    sample = [
        {"src": "192.168.1.2", "dst": "192.168.1.1", "len": 60},
        {"src": "10.0.0.5", "dst": "10.0.0.1", "len": 120},
    ]
    df = packets_to_dataframe(sample)
    print(df)
