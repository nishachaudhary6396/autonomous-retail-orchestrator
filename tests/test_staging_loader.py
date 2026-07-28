from app.ingestion.loader import DataLoader
from app.ingestion.validator import DataValidator
from app.ingestion.transformer import DataTransformer
from app.database.staging_loader import StagingLoader


loader = DataLoader("data/raw/Online_Retail.csv")
df = loader.load()

validator = DataValidator()
validator.validate(df)

transformer = DataTransformer()
df = transformer.transform(df)

staging = StagingLoader()

staging.load(df)