import polars as pl
from pathlib import Path
from app.config.constants import SCHEMA_OVERRIDES


class DataLoader:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self):

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"{self.file_path} not found."
            )

        df = pl.read_csv(
            self.file_path,
            schema_overrides=SCHEMA_OVERRIDES,
            infer_schema_length=10000,
        )

        return df