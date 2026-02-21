import sqlite3
import time
from queue import Queue
from typing import List, Tuple



class Logger:
  def __init__(self, db_path="cooker_log.db"):
    self.path = db_path
    conn = sqlite3.connect(self.path)
    cursor = conn.cursor()
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS curr_session (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp REAL NOT NULL,
                        curr_temp REAL NOT NULL,
                        target_temp REAL NOT NULL
                        )
                        """)
    conn.commit()
    conn.close()
    self.log_queue = Queue()

  # Helper methods
  def start_session(self) -> None:
    conn = sqlite3.connect(self.path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM curr_session")
    conn.commit()
    conn.close()

  def get_entries(self) -> List[Tuple[float, float, float]]:
    conn = sqlite3.connect(self.path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM curr_session ORDER BY timestamp ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows
  
  #def close(self) -> None:
  #  self.conn.close()


  # Controller
  def log(self, curr_temp: float, target_temp: float) -> None:
    """
    Record current and target temperatures with a timestamp in 'curr_session' db
    Push entry to queue for SSE updates
    
    :param curr_temp: Current temperature in Celsius; provided by SlowCookerMain call
    :param target_temp: Target temperature in Celsius; provided by SlowCookerMain call
    """
    timestamp = time.time()
    conn = sqlite3.connect(self.path)
    cursor = conn.cursor()
    cursor.execute(
      """INSERT INTO curr_session (timestamp, curr_temp, target_temp)
      VALUES (?, ?, ?)""",
      (timestamp, curr_temp, target_temp)
    )
    conn.commit()
    conn.close()
    self.log_queue.put({
      "timestamp": timestamp,
      "curr_temp": curr_temp,
      "target_temp": target_temp
    })

