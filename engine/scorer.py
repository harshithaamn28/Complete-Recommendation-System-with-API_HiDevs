class RecommendationScorer:

    def __init__(self):
        self.scorers = []

    def add_scorer(self, name, function, weight):
        self.scorers.append((name, function, weight))

    def calculate_score(self, user_id, item_id, context):
        total = 0
        explanation = {}

        for name, func, weight in self.scorers:
            score = func(user_id, item_id, context)
            total += score * weight
            explanation[name] = score

        return total, explanation

    def rank_candidates(self, user_id, candidates, limit=5):
        ranked = []

        for item in candidates:
            score, explanation = self.calculate_score(user_id, item, {})
            ranked.append((item, score, explanation))

        ranked.sort(key=lambda x: x[1], reverse=True)

        return ranked[:limit]