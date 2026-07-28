import polars as pl

from app.database.connection import engine


class StagingLoader:
    """
    Loads transformed data into the PostgreSQL staging table.
    """

    def load(
        self,
        df: pl.DataFrame,
        table_name: str = "staging_transactions"
    ):

        pandas_df = df.to_pandas()

        pandas_df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=10000,
        )

        print(
            f"{len(pandas_df)} rows loaded into '{table_name}'."
        )