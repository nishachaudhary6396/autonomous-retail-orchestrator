"""
✅ Final Approval tab.
"""

import streamlit as st


def render(approval: dict, state: dict):
    st.subheader("Final Approval")
    approved = approval.get("approved", False)

    if approved:
        st.success(f"✅ APPROVED by {approval.get('approver', 'N/A')}")
    else:
        st.error(f"❌ NOT APPROVED — {approval.get('approver', 'N/A')}")

    st.markdown("**Reason**")
    st.write(approval.get("reason", "No reason provided."))

    st.markdown("**Next Action**")
    st.write(approval.get("next_action", "No next action provided."))

    st.divider()
    with st.expander("Raw pipeline state (debug)"):
        st.json(state)
