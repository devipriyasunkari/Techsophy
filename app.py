import streamlit as st
from usage_monitor.monitor import fetch_sample_data
from cost_analysis.analyzer import detect_cost_anomalies
from optimizer.optimizer import suggest_optimizations

st.set_page_config(page_title="Cloud Cost Optimizer", layout="centered")
st.title("☁️ Automated Infrastructure Cost Optimization Tool")

if st.button("Run Cost Optimization"):
    # Step 1: Get usage data
    df = fetch_sample_data()
    st.success("✅ Sample usage data generated and saved.")

    # Step 2: Detect anomalies
    anomalies = detect_cost_anomalies()
    st.subheader("📉 Detected Cost Anomalies")
    if anomalies.empty:
        st.info("No anomalies detected.")
    else:
        st.dataframe(anomalies)

    # Step 3: Optimization Suggestions
    suggestions = suggest_optimizations(df)
    st.subheader("💡 Optimization Suggestions")
    if suggestions:
        for tip in suggestions:
            st.markdown(f"✔️ {tip}")
    else:
        st.info("No optimization suggestions found.")
 
