"""
🔍 Data Quality tab.
"""

import streamlit as st

from app.ui.helpers import badge


def render(quality_report: dict):
    st.subheader("Data Quality Report")
    score = quality_report.get("score")
    if score is not None:
        st.metric("Quality Score", f"{score}/100")
        st.progress(min(max(score, 0), 100) / 100)

    st.markdown(
        f"**Warehouse Approved:** {badge(quality_report.get('warehouse_approved', False), 'Approved', 'Not Approved')}"
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Critical Issues**")
        for issue in quality_report.get("critical_issues", []) or ["None reported."]:
            st.write(f"- {issue}")
    with c2:
        st.markdown("**Medium Issues**")
        for issue in quality_report.get("medium_issues", []) or ["None reported."]:
            st.write(f"- {issue}")
    with c3:
        st.markdown("**Low Priority Issues**")
        for issue in quality_report.get("low_priority_issues", []) or ["None reported."]:
            st.write(f"- {issue}")

    st.markdown("**Recommendations**")
    for rec in quality_report.get("recommendations", []) or ["None reported."]:
        st.write(f"- {rec}")

    if quality_report.get("reasoning"):
        with st.expander("Agent reasoning"):
            st.write(quality_report["reasoning"])
