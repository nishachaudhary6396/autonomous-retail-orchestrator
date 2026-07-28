import polars as pl


# Required columns expected in the retail dataset
REQUIRED_COLUMNS = {
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
}


# Date format used in the Online Retail dataset
DATE_FORMAT = "%m/%d/%Y %H:%M"


# Force these columns to be read as strings
SCHEMA_OVERRIDES = {
    "InvoiceNo": pl.String,
    "StockCode": pl.String,
    "CustomerID": pl.String,
}