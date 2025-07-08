def generate_report(anomalies, suggestions):
    print("\n📉 Detected Cost Anomalies:\n")
    if anomalies.empty:
        print("No anomalies detected.")
    else:
        print(anomalies)

    print("\n💡 Optimization Suggestions:\n")
    if suggestions:
        for tip in suggestions:
            print(f"✔️ {tip}")
    else:
        print("No optimization suggestions available.")
