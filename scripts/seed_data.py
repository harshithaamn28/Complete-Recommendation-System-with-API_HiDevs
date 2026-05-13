import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

# users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id TEXT PRIMARY KEY,
    name TEXT
)
""")

# content table
cur.execute("""
CREATE TABLE IF NOT EXISTS content(
    content_id TEXT PRIMARY KEY,
    title TEXT,
    category TEXT
)
""")

# skills table
cur.execute("""
CREATE TABLE IF NOT EXISTS skills(
    skill_id TEXT PRIMARY KEY,
    skill_name TEXT
)
""")

# interactions table
cur.execute("""
CREATE TABLE IF NOT EXISTS interactions(
    user_id TEXT,
    content_id TEXT,
    rating REAL,
    timestamp TEXT
)
""")

# feedback table
cur.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    user_id TEXT,
    content_id TEXT,
    feedback TEXT
)
""")

# metrics table
cur.execute("""
CREATE TABLE IF NOT EXISTS metrics(
    request_id TEXT,
    response_time REAL
)
""")

# sample users
users = [
    ("user1", "Alice"),
    ("user2", "Bob"),
    ("user3", "Charlie"),
    ("user4", "David"),
    ("user5", "Emma"),
    ("user6", "Frank"),
    ("user7", "Grace"),
    ("user8", "Helen"),
    ("user9", "Ian"),
    ("user10", "Jack")
]

cur.executemany(
    "INSERT OR IGNORE INTO users VALUES (?, ?)",
    users
)

# sample content
content = [
    ("c1", "Python Basics", "Programming"),
    ("c2", "Machine Learning", "AI"),
    ("c3", "Data Science", "AI"),
    ("c4", "Flask API", "Backend"),
    ("c5", "SQL Basics", "Database"),
    ("c6", "Pandas Tutorial", "Data"),
    ("c7", "NumPy Guide", "Data"),
    ("c8", "Streamlit App", "Frontend"),
    ("c9", "Docker Basics", "DevOps"),
    ("c10", "Git Tutorial", "Tools"),
    ("c11", "Linux Basics", "OS"),
    ("c12", "REST APIs", "Backend"),
    ("c13", "Statistics", "Math"),
    ("c14", "Deep Learning", "AI"),
    ("c15", "Data Visualization", "Data"),
    ("c16", "Testing with Pytest", "Testing"),
    ("c17", "Recommendation Systems", "AI"),
    ("c18", "Caching Concepts", "System"),
    ("c19", "Logging in Python", "System"),
    ("c20", "SQLite Tutorial", "Database")
]

cur.executemany(
    "INSERT OR IGNORE INTO content VALUES (?, ?, ?)",
    content
)

# sample interactions
interactions = [
    ("user1", "c1", 5, "2026-01-01"),
    ("user1", "c2", 4, "2026-01-02"),
    ("user2", "c2", 5, "2026-01-01"),
    ("user2", "c3", 4, "2026-01-03"),
    ("user3", "c1", 3, "2026-01-04"),
    ("user3", "c5", 5, "2026-01-05"),
    ("user4", "c4", 5, "2026-01-02"),
    ("user5", "c6", 4, "2026-01-03"),
    ("user6", "c7", 5, "2026-01-02"),
    ("user7", "c8", 4, "2026-01-04")
]

cur.executemany(
    "INSERT OR IGNORE INTO interactions VALUES (?, ?, ?, ?)",
    interactions
)

conn.commit()
conn.close()

print("Database initialized successfully")