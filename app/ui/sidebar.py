"""
Sidebar — pipeline controls (data upload + run pipeline + reset).
"""

import streamlit as st

from app.ui.pipeline import run_ingestion, run_profiling_and_analytics, run_agent_graph


def render_sidebar():
    with st.sidebar:
        st.title("🛒 Orchestrator")
        st.caption("Multi-agent LangGraph pipeline for retail inventory & demand")

        st.session_state.table_name = st.text_input(
            "Staging table name",
            value=st.session_state.table_name,
            help="Postgres table your data will be loaded into / read from.",
        )

        st.subheader("1. Load data (optional)")
        uploaded_file = st.file_uploader(
            "Upload a raw transaction export (.csv)",
            type=["csv"],
            help="Columns expected: InvoiceNo, StockCode, Description, "
            "Quantity, InvoiceDate, UnitPrice, CustomerID, Country",
        )

        load_clicked = st.button(
            "⬆️ Load into staging table",
            use_container_width=True,
            disabled=uploaded_file is None,
        )

        if load_clicked and uploaded_file is not None:
            with st.spinner("Loading, validating, transforming and staging your data..."):
                try:
                    n_rows = run_ingestion(uploaded_file, st.session_state.table_name)
                    st.success(f"Loaded {n_rows:,} rows into '{st.session_state.table_name}'.")
                except Exception as e:
                    st.error(f"Ingestion failed: {e}")

        st.subheader("2. Run the pipeline")
        st.caption(
            "Profiles and analyzes whatever is currently in the staging table, "
            "then runs it through your quality → warehouse → demand → "
            "inventory → approval agent graph."
        )
        run_clicked = st.button("▶️ Run full pipeline", type="primary", use_container_width=True)

        if run_clicked:
            try:
                with st.spinner("Profiling dataset..."):
                    profile, analytics = run_profiling_and_analytics(st.session_state.table_name)
                with st.spinner("Running agent pipeline (quality → warehouse → demand → inventory → approval)..."):
                    final_state = run_agent_graph(profile, analytics)
                st.session_state.final_state = final_state
                st.session_state.pipeline_ran = True
                st.success("Pipeline complete.")
            except Exception as e:
                st.session_state.pipeline_ran = False
                st.error(f"Pipeline failed: {e}")

        if st.session_state.pipeline_ran:
            st.divider()
            if st.button("🔄 Reset", use_container_width=True):
                st.session_state.pipeline_ran = False
                st.session_state.final_state = None
                st.rerun()
