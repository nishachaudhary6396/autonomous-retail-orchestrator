from app.ingestion.loader import DataLoader
from app.ingestion.validator import DataValidator
from app.ingestion.transformer import DataTransformer


loader = DataLoader("data/raw/Online_Retail.csv")
df = loader.load()

validator = DataValidator()
validator.validate(df)

transformer = DataTransformer()
clean_df = transformer.transform(df)

print(clean_df.head())
print()
print(clean_df.dtypes)
print()
print(clean_df.shape)

print("\nTransformation completed successfully!")