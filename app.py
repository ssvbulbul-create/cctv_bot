import os
import sys

print("Python version:", sys.version)
print("Starting...")

try:
    import flask
    print("✓ flask imported")
except Exception as e:
    print(f"✗ flask error: {e}")

try:
    import telegram
    print("✓ telegram imported")
except Exception as e:
    print(f"✗ telegram error: {e}")

try:
    import pandas as pd
    print("✓ pandas imported")
except Exception as e:
    print(f"✗ pandas error: {e}")

print("All imports checked!")

# Простой Flask сервер
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask on port {port}...")
    app.run(host="0.0.0.0", port=port)
