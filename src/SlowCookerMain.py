import time
from src.HeatController import HeatController
from src.TemperatureSensor import TemperatureSensor
from src.Logger import Logger
from src.RecipePresets import RecipePresets
from src.hardware.ssr import SSR
from src.hardware.MAX6675Amplifier import MAX6675Amplifier
from tests import mock_pi

DEBUG = True


class SlowCookerMain:
  def __init__(self, target_temp: int, cook_duration: int, logger: Logger):
    from src.website.app import app
    self.target_temp = target_temp
    self.cook_duration = cook_duration
    self.start_time = None
    self.thermometer = MAX6675Amplifier()
    self.heater = SSR()
    self.controller = HeatController(self.heater, self.target_temp)
    self.sensor = TemperatureSensor(self.thermometer)
    self.logger = logger
    self.web_interface = app
    #self.presets = RecipePresets()


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