DEBUG = True

try:
    import spidev # Requires SPI to be enabled in RPi
except ImportError:
    from tests.mock_pi import SpiDev

# Note, the numbers used for bus, device, speed, and mode are yet to be determined.
class MAX6675Amplifier:
    def __init__(self, spi, bus=0, device=0):
        if not spi is None:
            self.spi = spi
        else:
            self.spi = SpiDev()             # i don't think this is right for real spidev idk
        print(f"MAX6675Amplifier.py: SpiDev() called in init, self.spi id = {id(self.spi)}")
        self.spi.open(bus, device)
    
    def open(self, bus, device):
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 0
        self.spi.mode = 0b00

    # WIP
    def get_temp(self):
        if DEBUG:
            print("MAX6675Amplifier.py: get_temp() called, calling self.spi.xfer2()")
            print(f"MAX6675Amplifier.py: self.spi id = {id(self.spi)}")
        data = self.spi.xfer2()             # spi device returns two bytes
        raw = (data[0] << 8) | data[1]      # shift first byte and add it with second
        temp_c = raw * 0.25                 # !! convert to Celsius, will have to adjust per sensor's datasheet !!
        return temp_c

    def close(self):
        self.spi.close()