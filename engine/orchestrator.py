import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data.database import get_db


class RecommendationOrchestrator:

    def __init__(self):

        # cache storage
        self.cache = {}

    def get_recommendations(self, user_id):

        try:

            # return from cache if available
            if user_id in self.cache:
                return self.cache[user_id]

            # connect database
            conn = get_db()

            # read interactions table
            df = pd.read_sql_query(
                "SELECT * FROM interactions",
                conn
            )

            conn.close()

            # no data handling
            if df.empty:
                return []

            # create user-content interaction matrix
            matrix = df.pivot_table(
                index="user_id",
                columns="content_id",
                values="rating",
                fill_value=0
            )

            # cosine similarity
            similarity = cosine_similarity(matrix)

            # similarity dataframe
            similarity_df = pd.DataFrame(
                similarity,
                index=matrix.index,
                columns=matrix.index
            )

            # cold start handling
            if user_id not in similarity_df.index:

                popular_items = (
                    df.groupby("content_id")["rating"]
                    .mean()
                    .sort_values(ascending=False)
                    .head(5)
                    .index
                    .tolist()
                )

                final_recommendations = []

                for item in popular_items:

                    final_recommendations.append({
                        "content_id": item,
                        "reason": (
                            "Recommended because this content "
                            "is popular among users"
                        )
                    })

                # cache recommendations
                self.cache[user_id] = final_recommendations

                return final_recommendations

            # find similar users
            similar_users = similarity_df[user_id].sort_values(
                ascending=False
            )[1:4]

            recommendations = []

            for sim_user in similar_users.index:

                user_items = df[
                    df["user_id"] == sim_user
                ]["content_id"].tolist()

                recommendations.extend(user_items)

            # remove duplicates
            unique_items = list(set(recommendations))

            # limit top 5
            unique_items = unique_items[:5]

            final_recommendations = []

            # explanation generation
            for item in unique_items:

                final_recommendations.append({
                    "content_id": item,
                    "reason": (
                        "Recommended because similar users "
                        "interacted with this content"
                    )
                })

            # cache recommendations
            self.cache[user_id] = final_recommendations

            return final_recommendations

        except Exception as e:

            print(f"Recommendation error: {e}")

            return []