import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from api.app import app


def test_health():

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200


def test_recommendation():

    client = app.test_client()

    response = client.get("/recommend/user1")

    assert response.status_code == 200

    data = response.get_json()

    assert "recommendations" in data


def test_metrics():

    client = app.test_client()

    response = client.get("/metrics")

    assert response.status_code == 200


def test_feedback():

    client = app.test_client()

    response = client.post(
        "/feedback",
        json={
            "user": "user1",
            "item": "c1"
        }
    )

    assert response.status_code == 200