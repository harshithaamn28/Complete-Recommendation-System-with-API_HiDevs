import math

class RecommendationEvaluator:

    def precision_at_k(self, recommendations, relevant_items, k):
        if not recommendations:
            return 0

        rec_items = [item[0] for item in recommendations[:k]]
        relevant = set(relevant_items)

        hit = sum(1 for item in rec_items if item in relevant)

        return hit / k


    def recall_at_k(self, recommendations, relevant_items, k):
        if not relevant_items:
            return 0

        rec_items = [item[0] for item in recommendations[:k]]
        relevant = set(relevant_items)

        hit = sum(1 for item in rec_items if item in relevant)

        return hit / len(relevant)


    def ndcg_at_k(self, recommendations, relevant_items, k):
        dcg = 0
        rec_items = [item[0] for item in recommendations[:k]]
        relevant = set(relevant_items)

        for i, item in enumerate(rec_items):
            if item in relevant:
                dcg += 1 / math.log2(i + 2)

        idcg = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))

        return dcg / idcg if idcg > 0 else 0


    def evaluate_all(self, recommendations, relevant_items, k=5):
        return {
            "precision": self.precision_at_k(recommendations, relevant_items, k),
            "recall": self.recall_at_k(recommendations, relevant_items, k),
            "ndcg": self.ndcg_at_k(recommendations, relevant_items, k)
        }