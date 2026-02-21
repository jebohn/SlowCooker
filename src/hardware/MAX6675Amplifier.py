try:
    import spidev # Requires SPI to be enabled in RPi
except ImportError:
    from tests import mock_pi as spidev

# Note, the numbers used for bus, device, speed, and mode are yet to be determined.
class MAX6675Amplifier:
    def __init__(self, bus=0, device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
    
    def open(self, bus, device):
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 0
        self.spi.mode = 0b00

    # WIP
    def get_temp(self):
        data = self.spi.xfer2() # spi device returns two bytes
        raw = (data[0] << 8) | data[1]      # shift first byte and add it with second
        temp_c = raw * 0.25                 # convert to Celsius, will have to adjust per sensor's datasheet
        return temp_c

    def close(self):
        self.spi.close()