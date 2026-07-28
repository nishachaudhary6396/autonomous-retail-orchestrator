import polars as pl

from app.database.postgres_reader import PostgresReader


class DataProfiler:

    def __init__(self):
        self.reader = PostgresReader()

    def profile(
        self,
        table_name: str = "staging_transactions"
    ) -> dict:

        df = self.reader.read(table_name)

        profile = {

            "total_rows": df.height,

            "total_columns": df.width,

            "column_names": df.columns,

            "missing_values": {
                col: df[col].null_count()
                for col in df.columns
            },

            "duplicate_rows":
                df.height - df.unique().height,

            "cancelled_invoices":
                df.filter(
                    pl.col("InvoiceNo").str.starts_with("C")
                ).height,

            "negative_quantity":
                df.filter(
                    pl.col("Quantity") < 0
                ).height,

            "zero_quantity":
                df.filter(
                    pl.col("Quantity") == 0
                ).height,

            "negative_price":
                df.filter(
                    pl.col("UnitPrice") < 0
                ).height,

            "zero_price":
                df.filter(
                    pl.col("UnitPrice") == 0
                ).height,

            "unique_products":
                df["StockCode"].n_unique(),

            "unique_customers":
                df["CustomerID"].n_unique(),

            "unique_countries":
                df["Country"].n_unique(),

            "date_range": {

                "start": df["InvoiceDate"].min(),

                "end": df["InvoiceDate"].max(),

            }

        }

        return profile