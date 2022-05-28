from yoyo import step

__depends__ = {'0001_create_users_table'}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE users MODIFY password VARCHAR(500)
    """)


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE users MODIFY password VARCHAR(500) NOT NULL
    """)


steps = [
    step(apply_step, rollback_step)
]
