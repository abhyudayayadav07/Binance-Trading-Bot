from binance.client import Client
from config import API_KEY, API_SECRET

print(API_KEY[:10])
print(API_SECRET[:10])

client = Client(API_KEY, API_SECRET)

try:
    print(client.get_account())
except Exception as e:
    print(e)