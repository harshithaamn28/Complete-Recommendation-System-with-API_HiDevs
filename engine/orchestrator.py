from engine.candidate_gen import CandidateGenerator
from engine.scorer import RecommendationScorer
from data.database import get_db
import random


class RecommendationOrchestrator:

    def __init__(self):
        self.gen = CandidateGenerator()
        self.scorer = RecommendationScorer()
        self.cache = {}

        # scoring functions
        self.scorer.add_scorer(
            "relevance",
            lambda u, i, c: random.uniform(0.6, 1.0),
            0.7
        )

        self.scorer.add_scorer(
            "popularity",
            lambda u, i, c: random.uniform(0.4, 0.9),
            0.3
        )

    def get_recommendations(self, user_id, limit=5):

        # return cached result if exists
        if user_id in self.cache:
            return self.cache[user_id]

        # generate candidates
        candidates = self.gen.hybrid_candidates(user_id)

        # fetch past interactions (feedback learning)
        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT content_id FROM interactions WHERE user_id=?",
            (user_id,)
        )
        past_items = [row[0] for row in cur.fetchall()]
        conn.close()

        # rank candidates (fetch more for boosting)
        ranked = self.scorer.rank_candidates(user_id, candidates, limit * 2)

        # boost items based on feedback
        boosted = []
        for item, score, explanation in ranked:
            if item in past_items:
                score += 0.2

            boosted.append((item, score, explanation))

        # sort after boosting
        boosted.sort(key=lambda x: x[1], reverse=True)

        final = boosted[:limit]

        # cache result
        self.cache[user_id] = final

        return final