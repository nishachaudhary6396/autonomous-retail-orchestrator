import polars as pl

from app.database.postgres_reader import PostgresReader


class SalesAnalytics:

    def __init__(self):
        self.reader = PostgresReader()

    def analyze(
        self,
        table_name: str = "staging_transactions"
    ) -> dict:

        # Read data from PostgreSQL

        df = self.reader.read(table_name)

        # Keep only valid retail sales

        df = (
            df
            .filter(pl.col("Quantity") > 0)
            .filter(pl.col("UnitPrice") > 0)
            .filter(~pl.col("InvoiceNo").str.starts_with("C"))
            .filter(pl.col("Description").is_not_null())
        )

        # Revenue

        df = df.with_columns(
            (
                pl.col("Quantity") *
                pl.col("UnitPrice")
            ).alias("Revenue")
        )

        analytics = {

            # Overall KPIs

            "total_orders":
                df["InvoiceNo"].n_unique(),

            "total_products":
                df["StockCode"].n_unique(),

            "total_customers":
                df["CustomerID"].n_unique(),

            "total_revenue":
                round(
                    df["Revenue"].sum(),
                    2
                ),

            "average_order_value":
                round(
                    df["Revenue"].sum()
                    /
                    df["InvoiceNo"].n_unique(),
                    2
                ),

            # Top Selling Products

            "top_products":

                (
                    df
                    .group_by("Description")
                    .agg(
                        pl.col("Quantity")
                        .sum()
                        .alias("Quantity")
                    )
                    .sort(
                        "Quantity",
                        descending=True
                    )
                    .head(10)
                    .to_dicts()
                ),

            # Lowest Selling Products

            "bottom_products":

                (
                    df
                    .group_by("Description")
                    .agg(
                        pl.col("Quantity")
                        .sum()
                        .alias("Quantity")
                    )
                    .sort(
                        "Quantity"
                    )
                    .head(10)
                    .to_dicts()
                ),

            # Revenue by Country

            "country_sales":

                (
                    df
                    .group_by("Country")
                    .agg(
                        pl.col("Revenue")
                        .sum()
                        .alias("Revenue")
                    )
                    .sort(
                        "Revenue",
                        descending=True
                    )
                    .head(10)
                    .to_dicts()
                ),

            # Top Customers

            "top_customers":

                (
                    df
                    .group_by("CustomerID")
                    .agg(
                        pl.col("Revenue")
                        .sum()
                        .alias("Revenue")
                    )
                    .sort(
                        "Revenue",
                        descending=True
                    )
                    .head(10)
                    .to_dicts()
                ),

            # Monthly Revenue

            "monthly_sales":

                (
                    df
                    .with_columns(
                        pl.col("InvoiceDate")
                        .dt.strftime("%Y-%m")
                        .alias("Month")
                    )
                    .group_by("Month")
                    .agg(
                        pl.col("Revenue")
                        .sum()
                        .alias("Revenue")
                    )
                    .sort("Month")
                    .to_dicts()
                ),

        }

        return analytics