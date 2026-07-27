from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "mistral-small-latest")
    DATABASE_URL = os.getenv("DATABASE_URL")
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "chroma_db")


settings = Settings()