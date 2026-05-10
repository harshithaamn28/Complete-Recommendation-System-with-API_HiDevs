from data.database import get_db

class UserRepo:
    def get_user(self, user_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return cur.fetchone()

class InteractionRepo:
    def get_user_history(self, user_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT content_id FROM interactions WHERE user_id=?", (user_id,))
        return [row[0] for row in cur.fetchall()]

    def save_feedback(self, user_id, content_id, rating):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO interactions VALUES (?, ?, ?, datetime('now'))",
                    (user_id, content_id, rating))
        conn.commit()