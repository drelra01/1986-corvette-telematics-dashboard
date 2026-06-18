import sqlite3
from datetime import datetime

DB_NAME = "telematics.db"

def setup_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS car_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            rpm INTEGER,
            coolant_temp INTEGER,
            throttle INTEGER,
            battery REAL,
            speed INTEGER,
            engine_load REAL,
            battery_health TEXT,
            coolant_status TEXT
        )
    """)

    connection.commit()
    connection.close()

def save_car_data(data):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO car_data (
            time,
            rpm,
            coolant_temp,
            throttle,
            battery,
            speed,
            engine_load,
            battery_health,
            coolant_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data["rpm"],
        data["coolant_temp"],
        data["throttle"],
        data["battery"],
        data["speed"],
        data["engine_load"],
        data["battery_health"],
        data["coolant_status"]
    ))

    connection.commit()
    connection.close()

def get_recent_data():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM car_data
        ORDER BY id DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_trip_summary():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            COUNT(*) as total_records,
            ROUND(AVG(rpm), 1) as average_rpm,
            MAX(coolant_temp) as max_coolant,
            ROUND(AVG(battery), 2) as average_battery,
            MAX(speed) as max_speed,
            ROUND(AVG(engine_load), 1) as average_engine_load
        FROM car_data
    """)

    summary = cursor.fetchone()
    connection.close()
    return summary
            
