import polars as pl
from app.config.constants import REQUIRED_COLUMNS

class DataValidator:

    def validate(self, df: pl.DataFrame):

        missing = REQUIRED_COLUMNS - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        return True