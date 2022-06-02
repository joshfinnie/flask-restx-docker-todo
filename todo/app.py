import os

from flask import Flask

from todo.api import register_api

DEBUG = os.getenv("DEBUG", "").lower() == "true"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 5000)

app = Flask(__name__)

register_api(app)

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
