from data.database import get_db

def create_tables():
    conn = get_db()
    cur = conn.cursor()

    # Drop old tables (reset)
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP TABLE IF EXISTS content")
    cur.execute("DROP TABLE IF EXISTS interactions")
    cur.execute("DROP TABLE IF EXISTS skills")
    cur.execute("DROP TABLE IF EXISTS user_skills")
    cur.execute("DROP TABLE IF EXISTS content_skills")

    # USERS
    cur.execute("""
    CREATE TABLE users (
        id TEXT,
        name TEXT,
        interests TEXT,
        created_at TEXT
    )
    """)

    # CONTENT
    cur.execute("""
    CREATE TABLE content (
        id TEXT,
        title TEXT,
        category TEXT,
        difficulty TEXT,
        popularity REAL
    )
    """)

    # SKILLS
    cur.execute("""
    CREATE TABLE skills (
        id TEXT,
        name TEXT
    )
    """)

    # USER SKILLS
    cur.execute("""
    CREATE TABLE user_skills (
        user_id TEXT,
        skill_id TEXT,
        proficiency INTEGER
    )
    """)

    # CONTENT SKILLS
    cur.execute("""
    CREATE TABLE content_skills (
        content_id TEXT,
        skill_id TEXT
    )
    """)

    # INTERACTIONS
    cur.execute("""
    CREATE TABLE interactions (
        user_id TEXT,
        content_id TEXT,
        rating REAL,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()