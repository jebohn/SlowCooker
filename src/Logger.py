import sqlite3
import time
from queue import Queue
from typing import List, Tuple



class Logger:
  def __init__(self, db_path="cooker_log.db"):
    self.conn = sqlite3.connect(db_path)
    self.cursor = self.conn.cursor()

    self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS curr_session (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp REAL NOT NULL,
                        curr_temp REAL NOT NULL,
                        target_temp REAL NOT NULL
                        )
                        """)
    self.conn.commit()
    self.log_queue = Queue()

  # Helper methods
  def start_session(self) -> None:
    self.cursor.execute("DELETE FROM curr_session")
    self.conn.commit()

  def get_entries(self) -> List[Tuple[float, float, float]]:
    self.cursor.execute("SELECT * FROM curr_session ORDER BY timestamp ASC")
    return self.cursor.fetchall()
  
  def close(self) -> None:
    self.conn.close()


  # Controller
  def log(self, curr_temp: float, target_temp: float) -> None:
    """
    Record current and target temperatures with a timestamp in 'curr_session' db
    Push entry to queue for SSE updates
    
    :param curr_temp: Current temperature in Celsius; provided by SlowCookerMain call
    :param target_temp: Target temperature in Celsius; provided by SlowCookerMain call
    """
    timestamp = time.time()
    self.cursor.execute(
      """INSERT INTO curr_session (timestamp, curr_temp, target_temp)
      VALUES (?, ?, ?)""",
      (timestamp, curr_temp, target_temp)
    )
    self.conn.commit()

    log_queue.put({
      "timestamp": timestamp,
      "curr_temp": curr_temp,
      "target_temp": target_temp
    })

