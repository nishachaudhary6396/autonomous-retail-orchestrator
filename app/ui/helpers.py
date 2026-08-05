"""
Small display helper functions shared across tabs.
"""

import pandas as pd


def df_from_records(records, value_col=None):
    """Turn a list[dict] from your analytics/profile output into a
    DataFrame for charting. Returns None if there's nothing to show."""
    if not records:
        return None
    return pd.DataFrame(records)


def badge(ok: bool, true_label="Yes", false_label="No"):
    return f":green[**{true_label}**]" if ok else f":red[**{false_label}**]"
