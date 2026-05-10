from engine.orchestrator import RecommendationOrchestrator
from engine.evaluator import RecommendationEvaluator

# Test 1: recommendation generation
def test_recommendations_exist():
    engine = RecommendationOrchestrator()
    recs = engine.get_recommendations("user1")
    assert len(recs) > 0


# Test 2: ranking order (highest score first)
def test_recommendations_sorted():
    engine = RecommendationOrchestrator()
    recs = engine.get_recommendations("user1")

    scores = [item[1] for item in recs]
    assert scores == sorted(scores, reverse=True)


# Test 3: evaluator metrics
def test_evaluator_metrics():
    evaluator = RecommendationEvaluator()

    recs = [
        ("movie1", 0.9, {}),
        ("movie2", 0.8, {}),
        ("movie3", 0.7, {})
    ]

    relevant = ["movie1", "movie3"]

    result = evaluator.evaluate_all(recs, relevant, k=3)

    assert "precision" in result
    assert "recall" in result
    assert "ndcg" in result