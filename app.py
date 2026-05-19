from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route("/")
def home():
    return "CI/CD Pipeline Running Successfully 🚀"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)