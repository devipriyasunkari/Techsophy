from usage_monitor.monitor import fetch_sample_data
from cost_analysis.analyzer import detect_cost_anomalies
from optimizer.optimizer import suggest_optimizations
from recommender.recommend import generate_report

if __name__ == "__main__":
    print("🚀 Running Automated Infrastructure Cost Optimization Tool...\n")

    
    df = fetch_sample_data()

    
    anomalies = detect_cost_anomalies()

    
    suggestions = suggest_optimizations(df)

    
    generate_report(anomalies, suggestions)

