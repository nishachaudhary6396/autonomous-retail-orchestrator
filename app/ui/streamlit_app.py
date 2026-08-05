

"""Run from the project root with:

    streamlit run app/ui/streamlit_app.py
"""

import sys
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------
# Make "app.*" imports work regardless of where Streamlit is
# launched from (streamlit run rewrites sys.path[0] to this file's
# own folder, not the project root, so we add the project root
# explicitly).
# ---------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.ui.sidebar import render_sidebar
from app.ui.tabs import (
    analytics_tab,
    quality_tab,
    warehouse_tab,
    demand_tab,
    inventory_tab,
    approval_tab,
)


# =================================================================
# Page setup
# =================================================================
st.set_page_config(
    page_title="Autonomous Retail Inventory & Demand Orchestrator",
    page_icon="🛒",
    layout="wide",
)

if "pipeline_ran" not in st.session_state:
    st.session_state.pipeline_ran = False
if "final_state" not in st.session_state:
    st.session_state.final_state = None
if "table_name" not in st.session_state:
    st.session_state.table_name = "staging_transactions"


# =================================================================
# Sidebar — pipeline controls
# =================================================================
render_sidebar()


# =================================================================
# Main area
# =================================================================
st.title("Autonomous Retail Inventory & Demand Orchestrator")
st.caption(
    "Raw transaction data → PostgreSQL staging → data profiling & sales "
    "analytics → a LangGraph multi-agent pipeline that assesses data "
    "quality, warehouse readiness, demand, inventory plan, and final "
    "procurement approval."
)

if not st.session_state.pipeline_ran:
    st.info(
        "👈 Upload a CSV and/or click **Run full pipeline** in the sidebar "
        "to see live results here. Nothing on this page is pre-filled — "
        "every section below is populated from your pipeline's actual output."
    )
    st.stop()

state = st.session_state.final_state
profile = state.get("profile", {})
analytics = state.get("analytics", {})
quality_report = state.get("quality_report", {})
warehouse_report = state.get("warehouse_report", {})
demand_forecast = state.get("demand_forecast", {})
inventory_plan = state.get("inventory_plan", {})
approval = state.get("approval", {})

tabs = st.tabs(
    [
        "📊 Analytics",
        "🔍 Data Quality",
        "🏭 Warehouse Readiness",
        "📈 Demand Forecast",
        "📦 Inventory Plan",
        "✅ Final Approval",
    ]
)

with tabs[0]:
    analytics_tab.render(profile, analytics)

with tabs[1]:
    quality_tab.render(quality_report)

with tabs[2]:
    warehouse_tab.render(warehouse_report)

with tabs[3]:
    demand_tab.render(demand_forecast)

with tabs[4]:
    inventory_tab.render(inventory_plan)

with tabs[5]:
    approval_tab.render(approval, state)
