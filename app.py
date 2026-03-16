from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the Python microservice!"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/sum/<int:a>/<int:b>")
def sum_numbers(a, b):
    return jsonify({
        "result": a + b
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)