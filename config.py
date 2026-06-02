from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"

print("Looking for:", env_path)
print("File exists:", env_path.exists())

load_dotenv(env_path)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

print("KEY FOUND:", API_KEY is not None)
print("SECRET FOUND:", API_SECRET is not None)
