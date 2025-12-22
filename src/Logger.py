import time
from typing import List, Tuple

class Logger:
  def __init__(self):
    self.entries: List[Tuple[float, float, float]] = []

  # Get log entries
  def get_entries(self) -> List:
    return self.entries
  
  # Clear log
  def clear(self) -> None:
    self.entries.clear

  # Controller
  def log(self, curr_temp: float, target_temp: float, ) -> None:
    """
    Record current and target temperatures with a timestamp in 'entries' list
    
    :param curr_temp: Current temperature in Celsius; provided by SlowCookerMain call
    :param target_temp: Target temperature in Celsius; provided by SlowCookerMain call
    """
    if timestamp is None:
      timestamp = time.time()
    self.entries.append(timestamp, curr_temp, target_temp)