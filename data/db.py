import sqlite3
import pandas as pd


def setup_database(db_path="campaign_history.db"):
    """
    Sets up the database with necessary tables.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Campaign History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaign_history (
            campaign_id TEXT PRIMARY KEY,
            impressions INT,
            clicks INT,
            conversions FLOAT,
            spend REAL,
            revenue REAL,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Recommendations Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id TEXT,
            action TEXT,
            reason TEXT,
            metrics TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def store_campaign_history(df, db_path="campaign_history.db"):
    """
    Inserts campaign data into the campaign_history table, avoiding duplicates.
    """
    required_columns = ['campaign_id', 'impressions', 'clicks', 'conversions', 'spend', 'revenue', 'status']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Ensure numeric types for relevant columns
    numeric_columns = ['impressions', 'clicks', 'conversions', 'spend', 'revenue']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO campaign_history (campaign_id, impressions, clicks, conversions, spend, revenue, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (row['campaign_id'], row['impressions'], row['clicks'], row['conversions'], row['spend'], row['revenue'],
              row['status']))

    conn.commit()
    conn.close()


def store_recommendations(recommendations, db_path="campaign_history.db"):
    """
    Inserts recommendations into the recommendations table.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for rec in recommendations:
        cursor.execute('''
            INSERT INTO recommendations (campaign_id, action, reason, metrics)
            VALUES (?, ?, ?, ?)
        ''', (rec['campaign_id'], rec['action'], rec['reason'], str(rec['metrics'])))

    conn.commit()
    conn.close()


def retrieve_recommendations(db_path="campaign_history.db"):
    """
    Retrieves all recommendations from the recommendations table.
    """
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM recommendations"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

