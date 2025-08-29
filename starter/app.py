# starter/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Simple placeholder endpoint: convert plain notes into Q/A flashcards
@app.route("/api/flashcards", methods=["POST"])
def flashcards():
    """
    Expected JSON:
    { "notes": "line1\nline2\n..." }
    Returns JSON:
    { "cards": [ {"q": "...", "a": "..."}, ... ] }
    """
    data = request.get_json() or {}
    notes = data.get("notes", "").strip()
    if not notes:
        return jsonify({"error": "No notes provided"}), 400

    lines = [l.strip() for l in notes.splitlines() if l.strip()]
    # simple placeholder logic: turn first 5 lines into Q/A pairs
    cards = []
    for i, line in enumerate(lines[:5], start=1):
        q = f"What is point {i}?"
        a = line
        cards.append({"q": q, "a": a})
    return jsonify({"cards": cards})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
