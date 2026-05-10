from flask import Flask, jsonify, request, redirect
from engine.orchestrator import RecommendationOrchestrator
from data.database import get_db
import time
import uuid
import logging

# create app
app = Flask(__name__)
engine = RecommendationOrchestrator()

# logging setup
logging.basicConfig(level=logging.INFO)

# default route
@app.route("/")
def home():
    return redirect("/recommend/user1")


# recommendation API
@app.route("/recommend/<user_id>")
def recommend(user_id):

    request_id = str(uuid.uuid4())
    start = time.time()

    logging.info(f"Request {request_id} received for user {user_id}")

    if not user_id:
        logging.error("User ID missing")
        return jsonify({"error": "User ID missing"}), 400

    recs = engine.get_recommendations(user_id)

    if not recs:
        logging.warning(f"No recommendations for user {user_id}")
        return jsonify({"error": "No recommendations found"}), 404

    end = time.time()

    logging.info(f"Request {request_id} completed in {round(end-start,4)} sec")

    return jsonify({
        "request_id": request_id,
        "user": user_id,
        "recommendations": recs,
        "response_time": round(end - start, 4)
    })


# feedback API (UPDATED WITH DB STORAGE)
@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json

    if not data or "user" not in data or "item" not in data:
        logging.error("Invalid feedback request")
        return jsonify({"error": "Invalid request"}), 400

    try:
        conn = get_db()
        cur = conn.cursor()

        # store feedback
        cur.execute(
            "INSERT INTO interactions VALUES (?, ?, ?, datetime('now'))",
            (data["user"], data["item"], 5.0)
        )

        conn.commit()
        conn.close()

        logging.info(f"Feedback stored: {data}")

        return jsonify({"status": "feedback stored"})

    except Exception as e:
        logging.error(f"Error storing feedback: {e}")
        return jsonify({"error": "Failed to store feedback"}), 500


# health check
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# metrics
@app.route("/metrics")
def metrics():
    return jsonify({
        "cache_size": len(engine.cache)
    })


# run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)