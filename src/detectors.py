# detectors.py
# Contains multiple anomaly detection models

from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor

class AnomalyDetectors:
    def __init__(self):
        # Initialize models
        self.models = {
            "isolation_forest": IsolationForest(contamination=0.1, random_state=42),
            "one_class_svm": OneClassSVM(nu=0.1, kernel="rbf"),
            "lof": LocalOutlierFactor(n_neighbors=20, contamination=0.1, novelty=True)
        }

    def fit(self, X):
        for name, model in self.models.items():
            if name == "lof":
                model.fit(X)
            else:
                model.fit(X)

    def predict(self, X):
        """
        Returns a dictionary of model_name -> predictions
        1 = normal, -1 = anomaly
        """
        results = {}
        for name, model in self.models.items():
            results[name] = model.predict(X)
        return results

# Test detectors
if __name__ == "__main__":
    import pandas as pd
    sample_data = pd.DataFrame({
        "src": [192, 10, 172],
        "dst": [192, 10, 172],
        "len": [60, 120, 80]
    })
    ad = AnomalyDetectors()
    ad.fit(sample_data)
    preds = ad.predict(sample_data)
    print(preds)
