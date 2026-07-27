from sqlalchemy import text

from app.database.connection import engine

with engine.connect() as conn:
    version = conn.execute(text("SELECT version();"))
    print(version.scalar())

print("Database connected successfully!")