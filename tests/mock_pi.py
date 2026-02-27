class SpiDev:
  def __init__(self):
    self._temp_c = 25.0       # starting temp for test
  
  def open(self, bus, device):
    print(f"[MOCK SPI] open bus={bus}, device={device}")

  def xfer2(self):
    print(f"mock_pi.py: xfer2() called, self._temp_c = {self._temp_c}")
    value = int(self._temp_c / 0.25)
    msb = (value >> 8) & 0xFF
    lsb = value & 0xFF
    return[msb, lsb]

  def set_temp(self, on_time: int):
    print(f"mock_pi.py: set_temp() called, old self._temp_c = {self._temp_c}")
    # print(f"on_time = {on_time}, self._temp_c + on_time = {self._temp_c + on_time}")
    self._temp_c += on_time
    print(f"mock_pi.py: new self._temp_c = {self._temp_c}")

  def close(self):
    print("[MOCK SPI] close")


BCM = 'BCM'
OUT = 'OUT'
HIGH = 1
LOW = 0

_gpio_state = {}

def setmode(mode):
  print(f"[MOCK GPIO] setmode({mode})")

def setup(pin, mode, initial=None):
  _gpio_state[pin] = initial or LOW
  print(f"[MOCK GPIO] setup(pin={pin}, mode={mode})")

def output(pin, value):
  print(f"[MOCK GPIO] output(pin={pin}, value={value})")

