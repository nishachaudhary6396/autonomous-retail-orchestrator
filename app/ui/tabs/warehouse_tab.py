"""
🏭 Warehouse Readiness tab.
"""

import streamlit as st

from app.ui.helpers import badge


def render(warehouse_report: dict):
    st.subheader("Warehouse Readiness Report")
    ready = warehouse_report.get("ready_for_warehouse", False)
    risk = warehouse_report.get("risk_level", "Unknown")

    w1, w2 = st.columns(2)
    w1.markdown(f"**Ready for Warehouse:** {badge(ready)}")
    risk_color = {"low": "green", "medium": "orange", "high": "red"}.get(str(risk).lower(), "gray")
    w2.markdown(f"**Risk Level:** :{risk_color}[**{risk}**]")

    st.markdown("**Warehouse Actions**")
    for action in warehouse_report.get("warehouse_actions", []) or ["None reported."]:
        st.write(f"- {action}")

    st.markdown("**Rejected Tables**")
    rejected = warehouse_report.get("rejected_tables", [])
    if rejected:
        for t in rejected:
            st.write(f"- {t}")
    else:
        st.write("None.")

    if warehouse_report.get("summary"):
        st.markdown("**Summary**")
        st.write(warehouse_report["summary"])
