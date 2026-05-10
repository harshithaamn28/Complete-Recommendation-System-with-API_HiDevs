from engine.evaluator import RecommendationEvaluator

evaluator = RecommendationEvaluator()

recs = [
    ("movie1", 0.9, {}),
    ("movie2", 0.8, {}),
    ("movie3", 0.7, {}),
    ("movie4", 0.6, {}),
    ("movie5", 0.5, {})
]

relevant = ["movie1", "movie3"]

print(evaluator.evaluate_all(recs, relevant, k=5))