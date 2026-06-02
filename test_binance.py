from config import API_KEY, API_SECRET
from binance.client import Client

print(API_KEY is not None)
print(API_SECRET is not None)

client = Client(API_KEY, API_SECRET)

print("Client created successfully")