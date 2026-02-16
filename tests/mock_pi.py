class SpiDev:
  def __init__(self):
    self._temp_c = 25.0       # starting temp for test
  
  def open(self, bus, device):
    print(f"[MOCK SPI] open bus={bus}, device={device}.")

  def xfer2(self, data):
    value = int(self._temp_c / 0.25) << 3
    msb = (value << 8) & 0xFF
    lsb = value & 0xFF
    return[msb, lsb]

  def set_temp(self, on_time: int):
    for i in range[0, on_time]:
      self._temp_c += 1

  def close(self):
    print("[MOCK SPI] close.")


BCM = 'BCM'
OUT = 'OUT'
HIGH = 1
LOW = 0

def setmode(mode):
  print(f"[MOCK GPIO] setmode({mode})")

def setup(pin, mode):
  print(f"[MOCK GPIO] setup(pin={pin}, mode={mode})")

def output(pin, value):
  print(f"[MOCK GPIO] output(pin={pin}, value={value})")

