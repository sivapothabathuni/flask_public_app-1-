import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 🔹 Use the PORT variable
    app.run(host='0.0.0.0', port=port)        # 🔹 Bind to 0.0.0.0 so Render can access it
