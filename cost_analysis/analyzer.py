import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_cost_anomalies(filepath='data/sample_usage.csv'):
    df = pd.read_csv(filepath)
    pivot = df.pivot_table(index="Date", columns="Service", values="Cost", aggfunc='sum').fillna(0)
    
    # Use ML model to detect anomalies
    model = IsolationForest(contamination=0.25, random_state=42)
    pivot['anomaly'] = model.fit_predict(pivot)

    anomalies = pivot[pivot['anomaly'] == -1]
    return anomalies

