# toxicity_detector_app/main.py
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import logging
import os

app = Flask(__name__, template_folder="templates")

SIMULATE = os.getenv("SIMULATE_MODEL", "false").lower() == "true"
logger = logging.getLogger("toxicity")
logging.basicConfig(level=logging.INFO)

if not SIMULATE:
    classifier = pipeline("text-classification", model="unitary/toxic-bert")
else:
    classifier = None

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    logger.info(f"Received text: {text}")

    if SIMULATE:
        result = [{"label": "toxic", "score": 0.87}]
    else:
        result = classifier(text)

    logger.info(f"Result: {result}")
    return jsonify(result)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")