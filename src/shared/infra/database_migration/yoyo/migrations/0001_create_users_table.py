from yoyo import step


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(300) NOT NULL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(200) NOT NULL,
            password VARCHAR(500) NOT NULL
        )
    """)


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE users
    """)


steps = [
    step(apply_step, rollback_step)
]
