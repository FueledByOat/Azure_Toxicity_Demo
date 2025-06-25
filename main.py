from flask import Flask, request, jsonify, render_template
# from transformers import pipeline
import logging
import os
import random

app = Flask(__name__, template_folder="templates")

SIMULATE = os.getenv("SIMULATE_MODEL", "true").lower() == "true"
logger = logging.getLogger("toxicity")
logging.basicConfig(level=logging.INFO)

if not SIMULATE:
    try:
        classifier = pipeline("text-classification", model="unitary/toxic-bert")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        classifier = None
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
        result = [{"label": "toxic", "score": round(random.random()*100, 2)}]
    else:
        result = classifier(text)
    
    logger.info(f"Result: {result}")
    return jsonify(result)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    # Get port from environment variable (Azure sets this)
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)