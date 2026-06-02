from pathlib import Path
import os

print("Current file:", __file__)
print("Current working directory:", os.getcwd())

print("\nParent folder contents:")
for item in Path(__file__).resolve().parent.parent.iterdir():
    print(item.name)