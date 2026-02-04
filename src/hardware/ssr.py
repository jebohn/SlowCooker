import sys
sys.path.append('./tests')

try:
  import RPi.GPIO as GPIO     # Will only work when running on RPi
except ImportError:
  from tests import mock_pi as GPIO



class SSR:
  PIN = 10      # Placeholder number

  def __init__(self):
    self.state = False        # False = off, true = on
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN, GPIO.OUT)


  def get_ssr_state(self):
    """
    Get power state of SSR.
    """
    return self.state


  def on(self) -> None:
    """
    Turn SSR on via its pin.
    """
    GPIO.output(self.PIN, GPIO.HIGH)
    self.state = True


  def off(self) -> None:
    """
    Turn SSR off via its pin.
    """
    GPIO.output(self.PIN, GPIO.LOW)
    self.state = False