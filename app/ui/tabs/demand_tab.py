"""
📈 Demand Forecast tab.
"""

import streamlit as st


def render(demand_forecast: dict):
    st.subheader("Demand Forecast")
    if demand_forecast.get("forecast_summary"):
        st.write(demand_forecast["forecast_summary"])

    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("**🔥 High Demand**")
        for p in demand_forecast.get("high_demand_products", []) or ["None reported."]:
            st.write(f"- {p}")
    with d2:
        st.markdown("**➖ Medium Demand**")
        for p in demand_forecast.get("medium_demand_products", []) or ["None reported."]:
            st.write(f"- {p}")
    with d3:
        st.markdown("**🧊 Low Demand**")
        for p in demand_forecast.get("low_demand_products", []) or ["None reported."]:
            st.write(f"- {p}")

    st.markdown("**Recommended Reorder List**")
    for p in demand_forecast.get("recommended_reorder", []) or ["None reported."]:
        st.write(f"- {p}")

    if demand_forecast.get("reasoning"):
        with st.expander("Agent reasoning"):
            st.write(demand_forecast["reasoning"])
