from flask import Flask, request, jsonify, render_template
from logic import check_serum, check_moisturizer, check_sunscreen

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/serum", methods=["POST"])
def serum():
    data = request.json
    answer = data.get("answer")
    return jsonify(check_serum(answer))

@app.route("/moisturizer", methods=["POST"])
def moisturizer():
    data = request.json
    answer = data.get("answer")
    return jsonify(check_moisturizer(answer))

@app.route("/sunscreen", methods=["POST"])
def sunscreen():
    data = request.json
    answer = data.get("answer")
    return jsonify(check_sunscreen(answer))

# 🚨 MUST BE LAST
if __name__ == "__main__":
    app.run(debug=True, port=5001)
