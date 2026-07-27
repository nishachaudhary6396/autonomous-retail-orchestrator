import polars as pl
from pathlib import Path


class DataLoader:
    """
    Responsible for loading the raw dataset.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> pl.DataFrame:

        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found.")

        df = pl.read_csv(
            self.file_path,
            schema_overrides={
                "InvoiceNo": pl.String,
                "StockCode": pl.String,
                "CustomerID": pl.String,
            },
            try_parse_dates=True,
            infer_schema_length=10000,
        )

        return df