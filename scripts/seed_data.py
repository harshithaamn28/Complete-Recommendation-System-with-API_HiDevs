from data.models import create_tables
from data.database import get_db

create_tables()

conn = get_db()
cur = conn.cursor()

# USERS
for i in range(10):
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?, datetime('now'))",
        (f"user{i}", f"name{i}", "AI")
    )

# CONTENT
for i in range(20):
    cur.execute(
        "INSERT INTO content VALUES (?, ?, ?, ?, ?)",
        (f"movie{i}", f"title{i}", "AI", "easy", i * 0.1)
    )

# SKILLS
for i in range(5):
    cur.execute(
        "INSERT INTO skills VALUES (?, ?)",
        (f"skill{i}", f"skill_name{i}")
    )

# USER SKILLS
for i in range(10):
    cur.execute(
        "INSERT INTO user_skills VALUES (?, ?, ?)",
        (f"user{i}", f"skill{i%5}", 3)
    )

# CONTENT SKILLS
for i in range(20):
    cur.execute(
        "INSERT INTO content_skills VALUES (?, ?)",
        (f"movie{i}", f"skill{i%5}")
    )

# INTERACTIONS
for i in range(10):
    cur.execute(
        "INSERT INTO interactions VALUES (?, ?, ?, datetime('now'))",
        (f"user{i}", f"movie{i}", 4.0)
    )

conn.commit()
conn.close()

print("Database seeded")