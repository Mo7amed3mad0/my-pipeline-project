from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 App is running successfully!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"➕ {a} + {b} = {a + b}"

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return f"➖ {a} - {b} = {a - b}"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f"✖️ {a} × {b} = {a * b}"

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return f"➗ {a} ÷ {b} = {a / b}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)