from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Internal Status App is running."


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "internal-status-app"
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)