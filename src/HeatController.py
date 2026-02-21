import time

#  !!  VARIABLES INSIDE compute_pid() WILL NEED  !!
#  !!    ADJUSTMENT BASED ON CROCK-POT TRIALS    !!



class HeatController:
  # WINDOW constant might need adjustment
  WINDOW = 10.0

  def __init__(self, heater, target_temp: float):
    self.heater = heater              # SSR instance, supplied by SlowCookerMain.py
    self.target_temp = target_temp
    self.last_err = 0.0
    self.last_time = None
    self.integral_total = 0.0
    self.curr_temp = 0.0
    self.power_state = False          # False = off, true = on


  # Getters and Setters
  def get_power_state(self) -> bool:
    return self.power_state

  def get_target(self) -> float:
    return self.target_temp
  
  def set_target_temp(self, target_temp: float) -> None:
    self.target_temp = target_temp

  def set_curr_temp(self, curr_temp: float) -> None:
    self.curr_temp = curr_temp


  # Helper Methods
  def power_on(self) -> None:
    self.heater.on()
    self.power_state = True
  
  def power_off(self) -> None:
    self.heater.off()
    self.power_state = False

  def compute_pid(self) -> float:
    """
    Computes output percentage based on current temperature to
    reach target temperature.
    
    :param dt: Time elapsed since last PID computation in seconds.
    :return: Output percentage representing proportion of WINDOW
              that heater should be on.
    """
    # adjust kp, ki, kd like so (per real crockpot trials):
    #   major overshoot -> reduce kp
    #   never reaches target_temp -> increase ki slowly
    #   oscillates slowly -> reduce kp or ki
    KP = 0.5
    KI = 0.05
    KD = 0.01

    now = time.perf_counter()
    if self.prev_time is None:
      dt = 1  # default for first iteration
    else:
      dt = now - self.prev_time
    self.prev_time = now

    err = self.target_temp - self.curr_temp
    proportional = KP * err

    # Might need to max/min bound this value, will see with trials
    #   e.g., self.integral_total = max(min(self.integral_total, 10.0), -10.0)
    self.integral_total += KI * err * dt

    derivative = (KD * (err - self.last_err)) / dt
    self.last_err = err

    output = proportional + self.integral_total + derivative

    return max(0.0, min(output, 1.0))
  
  
  # Controller
  def cycle(self, test) -> None:
    """
    Cycles SSR on and off, per PID output, for WINDOW time.
    
    :param output: Output percentage from compute_pid().
    """

    output = self.compute_pid(self)

    on_time = output * self.WINDOW
    off_time = self.WINDOW - on_time

    if test is not None:
      test.set_temp(on_time)

    if on_time > 0:
      self.power_on()
      time.sleep(on_time)

    if off_time > 0:
      self.power_off()
      time.sleep(off_time)


