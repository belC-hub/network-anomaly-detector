# src/preprocess.py
import pandas as pd

def packets_to_dataframe(packets):
    """
    Converts list of packet dicts to a DataFrame.
    """
    df = pd.DataFrame(packets)
    
    # Convert src/dst IPs to numeric representation
    df['src_num'] = df['src'].apply(lambda x: sum([int(i) for i in x.split('.')]))
    df['dst_num'] = df['dst'].apply(lambda x: sum([int(i) for i in x.split('.')]))
    
    return df
