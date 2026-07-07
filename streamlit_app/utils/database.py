import sqlite3
from pathlib import Path
from auth.security import hash_password

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_DIR / "bluestock_mf.db"
print(DB_PATH)

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        mobile TEXT UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def create_user(username, email, mobile, password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, email, mobile, password_hash)
            VALUES (?, ?, ?, ?)
            """,
            (username, email, mobile, password_hash)
        )

        conn.commit()
        print("User Saved Successfully")
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def get_user(username_or_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE username = ? OR email = ?
    """, (username_or_email, username_or_email))

    user = cursor.fetchone()

    conn.close()

    return user

def get_dashboard_kpis():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM fact_performance")
    total_schemes = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(aum_crore) FROM fact_performance")
    total_aum = cursor.fetchone()[0]

    # Average 1 Year Return
    cursor.execute("SELECT AVG(return_1yr_pct) FROM fact_performance")
    avg_return = cursor.fetchone()[0]

    cursor.execute("""
        SELECT risk_grade, COUNT(*)
        FROM fact_performance
        GROUP BY risk_grade
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    risk = cursor.fetchone()[0]

    conn.close()

    return total_schemes, total_aum, avg_return, risk

def get_all_funds():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT scheme_name
        FROM fact_performance
        ORDER BY scheme_name
    """)

    funds = [row[0] for row in cursor.fetchall()]

    conn.close()

    return funds

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def update_password(email, password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET password_hash = ?
        WHERE email = ?
        """,
        (password_hash, email)
    )

    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE LOWER(email)=LOWER(?)",
        (email,)
    )

    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_mobile(mobile):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE mobile=?",
        (mobile,)
    )

    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email_mobile(email, mobile):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE LOWER(email)=LOWER(?)
        AND mobile=?
        """,
        (email, mobile)
    )

    user = cursor.fetchone()
    conn.close()
    return user

def get_fund_details(scheme_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            scheme_name,
            fund_house,
            category,
            plan,
            return_1yr_pct,
            return_3yr_pct,
            return_5yr_pct,
            aum_crore,
            expense_ratio_pct,
            risk_grade
        FROM fact_performance
        WHERE scheme_name = ?
    """, (scheme_name,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return {
        "scheme_name": row[0],
        "fund_house": row[1],
        "category": row[2],
        "plan": row[3],
        "return_1yr": row[4],
        "return_3yr": row[5],
        "return_5yr": row[6],
        "aum": row[7],
        "expense": row[8],
        "risk": row[9]
    }

def get_filtered_funds(fund_house="All", category="All", risk="All"):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT scheme_name
        FROM fact_performance
        WHERE 1=1
    """

    params = []

    if fund_house != "All":
        query += " AND fund_house = ?"
        params.append(fund_house)

    if category != "All":
        query += " AND category = ?"
        params.append(category)

    if risk != "All":
        query += " AND risk_grade = ?"
        params.append(risk)

    query += " ORDER BY scheme_name"

    cursor.execute(query, params)

    funds = [row[0] for row in cursor.fetchall()]

    conn.close()

    return funds

