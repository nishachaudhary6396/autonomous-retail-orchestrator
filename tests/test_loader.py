from app.ingestion.loader import DataLoader
from app.ingestion.validator import DataValidator

loader = DataLoader("data/raw/Online_Retail.csv")

df = loader.load()

validator = DataValidator()

validator.validate(df)

print(df.head(30))

print(df.shape)

print("Dataset loaded successfully!")