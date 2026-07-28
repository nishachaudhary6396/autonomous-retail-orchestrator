import polars as pl

from app.config.constants import DATE_FORMAT


class DataTransformer:
  

    def transform(self, df: pl.DataFrame) -> pl.DataFrame:

        df = df.with_columns(

            # Convert InvoiceDate -> Datetime
            pl.col("InvoiceDate")
            .str.strptime(
                pl.Datetime,
                format=DATE_FORMAT,
                strict=False,
            ),

            # Convert numeric columns
            pl.col("Quantity").cast(pl.Int64),
            pl.col("UnitPrice").cast(pl.Float64),

            # Clean string columns
            pl.col("Description")
            .str.strip_chars()
            .str.replace_all(r"\s+", " ")
            .replace("", None),

            pl.col("Country")
            .str.strip_chars()
            .str.to_titlecase()
            .replace("", None),

            pl.col("InvoiceNo")
            .str.strip_chars(),

            pl.col("StockCode")
            .str.strip_chars(),

            pl.col("CustomerID")
            .str.strip_chars()
            .replace("", None),
        )

        return df