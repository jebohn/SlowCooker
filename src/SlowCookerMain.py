import time
import HeatController
import TemperatureSensor
import Logger
from website.app import app
import RecipePresets
from hardware.ssr import SSR
from hardware.MAX6675Amplifier import MAX6675Amplifier
from tests import mock_pi

DEBUG = True


class SlowCookerMain:
  def __init__(self, target_temp: int, cook_duration: int, logger: Logger):
    self.target_temp = target_temp
    self.cook_duration = cook_duration
    self.start_time = None
    self.thermometer = MAX6675Amplifier()
    self.heater = SSR()
    self.controller = HeatController(self.heater, self.target_temp)
    self.sensor = TemperatureSensor()
    self.logger = logger
    self.web_interface = app()
    self.presets = RecipePresets()


  # Helper method
  def start_session(self) -> None:
    self.start_time = time.perf_counter()
    self.controller.set_target_temp(self.target_temp)
    curr_temp = self.sensor.read_temp()
    self.controller.set_curr_temp(curr_temp)
    self.logger.start_session()
    self.logger.log(curr_temp, self.target_temp)


  # Controller; runs program in loop for given cook time
  def run(self) -> None:
    self.start_session()
    end_time = self.start_time + self.cook_duration

    if DEBUG is True:
      test = mock_pi.SpiDev()
    else:
      test = None

    while time.perf_counter() < end_time:
      self.controller.cycle(test)
      curr_temp = self.sensor.read_temp()
      self.controller.set_curr_temp(curr_temp)
      self.logger.log(curr_temp, self.target_temp)
    
    # if user wants keep warm:
    #   run keep warm preset indefinitely
    # else:
    self.heater.off()
    self.logger.close()


# I'm not sure there will be a need for a main() once the API is completed
# The API would basically handle the usual responsibilites of a main(), no?
# if __name__ == "__main__":
#   # Hard code for testing
#   target_temp = float(input("Enter target temperature (Celsius): "))
#   cook_duration = int(input("Enter cook duration (minutes): ")) * 60

#   cooker = SlowCookerMain(target_temp, cook_duration)
#   cooker.run()