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

from engine.orchestrator import RecommendationOrchestrator


def test_recommendations():

    engine = RecommendationOrchestrator()

    recs = engine.get_recommendations("user1")

    assert isinstance(recs, list)

    assert len(recs) > 0


def test_cold_start():

    engine = RecommendationOrchestrator()

    recs = engine.get_recommendations("new_user")

    assert isinstance(recs, list)

    assert len(recs) > 0