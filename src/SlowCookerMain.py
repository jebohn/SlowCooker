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
    self.cook_duration = cook_duration        # !! must add operation to multiply by 60 to get minutes !!
    self.start_timestamp = None
    self.start_time = None
    self.thermometer = None
    self.heater = None
    self.controller = None
    self.sensor = None
    self.logger = logger
    self.web_interface = app
    #self.presets = RecipePresets()         # !! not yet implemented, must complete !!


  # Helper method
  def start_session(self) -> None:
    self.start_timestamp = time.time()
    self.start_time = time.perf_counter()
    self.controller.set_target_temp(self.target_temp)
    curr_temp = self.sensor.read_temp()
    print(f"SlowCookerMain.py initialize curr_temp in start_session() as {curr_temp}")
    self.controller.set_curr_temp(curr_temp)
    self.logger.start_session()
    self.logger.start_timestamp(self.start_timestamp)
    self.logger.log(curr_temp, self.target_temp)


  # Controller; runs program in loop for given cook time
  def run(self) -> None:
    self.thermometer = MAX6675Amplifier()
    self.heater = SSR()
    self.controller = HeatController(self.heater, self.target_temp)
    self.sensor = TemperatureSensor(self.thermometer)
    self.start_session()
    end_time = self.start_time + self.cook_duration

    if DEBUG is True:
      test = mock_pi.SpiDev()
    else:
      test = None

    while time.perf_counter() < end_time:
      self.controller.cycle(test)
      if DEBUG:
        print("SlowCookerMain.py: Calling self.sensor.read_temp")
      curr_temp = self.sensor.read_temp()
      if DEBUG:
        print(f"SlowCookerMain.py: curr_temp = {curr_temp}")
      self.controller.set_curr_temp(curr_temp)
      print(curr_temp, " : ", self.target_temp)
      self.logger.log(curr_temp, self.target_temp)
    
    # if user wants keep warm:
    #   run keep warm preset indefinitely
    # else:
    self.heater.off()
    #self.logger.close()