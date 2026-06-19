from database import engine
from sqlalchemy import text


def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ MySQL Connected")
            print("Result:", result.fetchone())

    except Exception as e:
        print("❌ Connection Failed")
        print(e)


test_connection()