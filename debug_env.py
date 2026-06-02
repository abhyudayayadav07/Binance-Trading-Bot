from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).resolve().parent.parent / ".env"

print("ENV PATH:", env_path)
print("EXISTS:", env_path.exists())

load_dotenv(env_path)

print("BINANCE_API_KEY =", os.getenv("BINANCE_API_KEY"))
print("BINANCE_API_SECRET =", os.getenv("BINANCE_API_SECRET"))