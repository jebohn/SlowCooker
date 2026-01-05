import sys
sys.path.append('./hardware')

import time
import HeatController
import Logger
import WebInterfaceAPI
import RecipePresets
import SSR
import MAX6675Amplifier

class SlowCookerMain:
  def __init__(self, target_temp: int, cook_duration: int):
    self.thermometer = MAX6675Amplifier()
    self.heater = SSR()
    self.controller = HeatController(self.heater, target_temp)
    self.logger = Logger()
    self.web_interface = WebInterfaceAPI()
    self.presets = RecipePresets()
    self.start_time = time.perf_counter()
    self.cook_duration = cook_duration

  # Helper methods
  def update_log() -> None:
    pass

  def start_session(target_temp: float, cook_duration: int) -> None:
    pass

  # method to keep warm after run loop completes? should keep warm be a recipe preset?

  # Controller; runs program in loop for given cook time
  def run(target_temp: float, cook_duration: int) -> None:
    pass




  # main() HERE OR IN main.py FILE?
  #
  # if __name__ == "__main__":
  #   main()