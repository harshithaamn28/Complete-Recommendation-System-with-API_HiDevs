from flask import Flask, jsonify, request, redirect
from engine.orchestrator import RecommendationOrchestrator
from data.database import get_db
import time
import uuid
import logging

# create app
app = Flask(__name__)

# initialize engine
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

    logging.info(
        f"Request {request_id} received for user {user_id}"
    )

    # validation
    if not user_id:

        logging.error("User ID missing")

        return jsonify({
            "error": "User ID missing"
        }), 400

    try:

        # get recommendations
        recs = engine.get_recommendations(user_id)

        end = time.time()

        response_time = round(end - start, 4)

        logging.info(
            f"Request {request_id} completed "
            f"in {response_time} sec"
        )

        return jsonify({
            "request_id": request_id,
            "user": user_id,
            "recommendations": recs,
            "response_time": response_time
        })

    except Exception as e:

        logging.error(
            f"Recommendation error: {e}"
        )

        return jsonify({
            "error": "Recommendation failed"
        }), 500


# feedback API
@app.route("/feedback", methods=["POST"])
def feedback():

    data = request.json

    # validation
    if not data:

        return jsonify({
            "error": "No JSON payload received"
        }), 400

    if "user" not in data or "item" not in data:

        return jsonify({
            "error": "Missing user or item"
        }), 400

    try:

        conn = get_db()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO feedback
            VALUES (?, ?, ?)
            """,
            (
                data["user"],
                data["item"],
                "positive"
            )
        )

        conn.commit()

        conn.close()

        logging.info(
            f"Feedback stored: {data}"
        )

        return jsonify({
            "status": "feedback stored"
        })

    except Exception as e:

        logging.error(
            f"Feedback error: {e}"
        )

        return jsonify({
            "error": "Feedback storage failed"
        }), 500


# health check
@app.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


# metrics endpoint
@app.route("/metrics")
def metrics():

    return jsonify({
        "cache_size": len(engine.cache),
        "api_status": "running"
    })


# run app
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )