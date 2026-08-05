"""
📦 Inventory Plan tab.
"""

import streamlit as st


def render(inventory_plan: dict):
    st.subheader("Inventory Plan")
    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown("**🚨 Priority Reorders**")
        for p in inventory_plan.get("priority_reorders", []) or ["None reported."]:
            st.write(f"- {p}")
    with i2:
        st.markdown("**📦 Standard Reorders**")
        for p in inventory_plan.get("standard_reorders", []) or ["None reported."]:
            st.write(f"- {p}")
    with i3:
        st.markdown("**🚫 No Reorder**")
        for p in inventory_plan.get("no_reorder_products", []) or ["None reported."]:
            st.write(f"- {p}")

    st.markdown("**Warehouse Actions**")
    for a in inventory_plan.get("warehouse_actions", []) or ["None reported."]:
        st.write(f"- {a}")

    if inventory_plan.get("procurement_summary"):
        st.markdown("**Procurement Summary**")
        st.write(inventory_plan["procurement_summary"])

    if inventory_plan.get("reasoning"):
        with st.expander("Agent reasoning"):
            st.write(inventory_plan["reasoning"])
