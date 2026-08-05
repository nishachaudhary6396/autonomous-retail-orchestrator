"""
📊 Analytics tab — dataset profile + sales analytics charts.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from app.ui.helpers import df_from_records


def render(profile: dict, analytics: dict):
    st.subheader("Dataset Profile")
    p1, p2, p3, p4 = st.columns(4)
    p1.metric("Total Rows", f"{profile.get('total_rows', 0):,}")
    p2.metric("Unique Products", f"{profile.get('unique_products', 0):,}")
    p3.metric("Unique Customers", f"{profile.get('unique_customers', 0):,}")
    p4.metric("Unique Countries", f"{profile.get('unique_countries', 0):,}")

    p5, p6, p7, p8 = st.columns(4)
    p5.metric("Duplicate Rows", f"{profile.get('duplicate_rows', 0):,}")
    p6.metric("Cancelled Invoices", f"{profile.get('cancelled_invoices', 0):,}")
    p7.metric("Negative Quantity Rows", f"{profile.get('negative_quantity', 0):,}")
    p8.metric("Zero/Negative Price Rows",
              f"{profile.get('zero_price', 0) + profile.get('negative_price', 0):,}")

    date_range = profile.get("date_range", {})
    if date_range:
        st.caption(f"Date range: {date_range.get('start')} → {date_range.get('end')}")

    missing = profile.get("missing_values", {})
    if missing:
        with st.expander("Missing values by column"):
            st.dataframe(
                pd.DataFrame(
                    {"column": list(missing.keys()), "missing_count": list(missing.values())}
                ),
                use_container_width=True,
                hide_index=True,
            )

    st.divider()
    st.subheader("Sales Analytics")
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Total Orders", f"{analytics.get('total_orders', 0):,}")
    a2.metric("Total Revenue", f"£{analytics.get('total_revenue', 0):,.2f}")
    a3.metric("Avg Order Value", f"£{analytics.get('average_order_value', 0):,.2f}")
    a4.metric("Total Customers", f"{analytics.get('total_customers', 0):,}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Top 10 Products (by quantity sold)**")
        df_top = df_from_records(analytics.get("top_products"))
        if df_top is not None:
            fig = px.bar(df_top, x="Quantity", y="Description", orientation="h")
            fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=380)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.caption("No data.")

        st.markdown("**Top 10 Customers (by revenue)**")
        df_cust = df_from_records(analytics.get("top_customers"))
        if df_cust is not None:
            df_cust["CustomerID"] = df_cust["CustomerID"].astype(str)
            fig = px.bar(df_cust, x="Revenue", y="CustomerID", orientation="h")
            fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=380)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.caption("No data.")

    with col2:
        st.markdown("**Bottom 10 Products (by quantity sold)**")
        df_bottom = df_from_records(analytics.get("bottom_products"))
        if df_bottom is not None:
            fig = px.bar(df_bottom, x="Quantity", y="Description", orientation="h")
            fig.update_layout(yaxis={"categoryorder": "total descending"}, height=380)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.caption("No data.")

        st.markdown("**Revenue by Country (top 10)**")
        df_country = df_from_records(analytics.get("country_sales"))
        if df_country is not None:
            fig = px.bar(df_country, x="Revenue", y="Country", orientation="h")
            fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=380)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.caption("No data.")

    st.markdown("**Monthly Revenue**")
    df_monthly = df_from_records(analytics.get("monthly_sales"))
    if df_monthly is not None:
        fig = px.line(df_monthly, x="Month", y="Revenue", markers=True)
        fig.update_layout(height=380)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.caption("No data.")
