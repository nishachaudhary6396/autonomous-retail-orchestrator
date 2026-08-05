"""
Pipeline helper functions.
---------------------------
Thin wrappers around your real ingestion / profiling / analytics /
LangGraph classes. No data is invented here — these functions just
call your existing app.* code and return its output.
"""

import tempfile

from app.ingestion.loader import DataLoader
from app.ingestion.validator import DataValidator
from app.ingestion.transformer import DataTransformer
from app.database.staging_loader import StagingLoader
from app.profiling.profiler import DataProfiler
from app.analytics.sales_analytics import SalesAnalytics
from app.graph.graph import graph


def run_ingestion(uploaded_file, table_name: str):
    """Persist the uploaded CSV, then load -> validate -> transform ->
    write it into the Postgres staging table using your real classes."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    df = DataLoader(tmp_path).load()
    DataValidator().validate(df)
    df = DataTransformer().transform(df)
    StagingLoader().load(df, table_name=table_name)
    return len(df)


def run_profiling_and_analytics(table_name: str):
    profile = DataProfiler().profile(table_name=table_name)
    analytics = SalesAnalytics().analyze(table_name=table_name)
    return profile, analytics


def run_agent_graph(profile: dict, analytics: dict):
    initial_state = {
        "profile": profile,
        "analytics": analytics,
        "quality_report": {},
        "warehouse_report": {},
        "demand_forecast": {},
        "inventory_plan": {},
        "approval": {},
    }
    return graph.invoke(initial_state)
