# judge.py
# Combines multiple model predictions into a final decision

import pandas as pd
from collections import Counter

def majority_vote(predictions_dict):
    """
    predictions_dict: dict of model_name -> array of predictions (1 = normal, -1 = anomaly)
    Returns: a pandas Series with final decision for each sample
    """
    # Transpose dict so we get a list of predictions per sample
    df = pd.DataFrame(predictions_dict)
    
    final_decision = []
    for i in range(len(df)):
        votes = df.iloc[i].values
        counts = Counter(votes)
        # -1 = anomaly, 1 = normal
        final = -1 if counts[-1] > counts[1] else 1
        final_decision.append(final)
    
    return pd.Series(final_decision, name="final_decision")

# Test judge
if __name__ == "__main__":
    sample_preds = {
        "isolation_forest": [1, -1, 1],
        "one_class_svm": [1, -1, -1],
        "lof": [1, 1, -1]
    }
    result = majority_vote(sample_preds)
    print(result)
