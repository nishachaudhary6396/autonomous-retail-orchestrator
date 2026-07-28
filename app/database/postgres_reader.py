import polars as pl

from app.database.connection import engine


class PostgresReader:
    """
    Reads data from PostgreSQL.
    """

    def read(
        self,
        table_name: str = "staging_transactions"
    ) -> pl.DataFrame:

        query = f"SELECT * FROM {table_name}"

        df = pl.read_database(
            query=query,
            connection=engine,
        )

        return df