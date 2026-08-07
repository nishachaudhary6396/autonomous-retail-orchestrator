from pydantic_settings import BaseSettings, SettingsConfigDict
import streamlit as st
import os


class Settings(BaseSettings):
    GROQ_API_KEY: str
    MODEL_NAME: str = "llama-3.3-70b-versatile"
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


# Debugging (temporary)
st.write("GROQ_API_KEY exists:", "GROQ_API_KEY" in os.environ)
st.write("DATABASE_URL exists:", "DATABASE_URL" in os.environ)
st.write("MODEL_NAME exists:", "MODEL_NAME" in os.environ)

try:
    settings = Settings()
except Exception as e:
    st.exception(e)
    raise