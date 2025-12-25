from random import randint
from pswd_logic import generate_password
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home page route (browser loads this)
@app.route("/")
def home():
    return render_template("index.html")

# API route (JS calls this)
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = randint(int(data.get("min_length",9)),int(data.get("max_length",12)))
    symbols = data.get("symbols", True)

    password = generate_password(length, symbols)
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=10000)
