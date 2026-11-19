from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('APP_VERSION', 'v1')
    return f"Hello from the DevOps E2E Pipeline! Running version: {version}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
