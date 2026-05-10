class CandidateGenerator:

    def collaborative_candidates(self, user_id):
        return ["movie1", "movie2", "movie3"]

    def content_based_candidates(self, user_id):
        return ["movie2", "movie4", "movie5"]

    def popularity_candidates(self):
        return ["movie3", "movie5", "movie6"]

    def hybrid_candidates(self, user_id):
        candidates = (
            self.collaborative_candidates(user_id) +
            self.content_based_candidates(user_id) +
            self.popularity_candidates()
        )
        return list(set(candidates))[:20]