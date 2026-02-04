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