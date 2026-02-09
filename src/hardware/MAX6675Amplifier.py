try:
    import spidev # Requires SPI to be enabled in RPi
except ImportError:
    from tests import mock_pi as spidev

# Note, the numbers used for bus, device, speed, and mode are yet to be determined.
class MAX6675Amplifier:
    def __init__(self, bus=0, device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
    
    def open(self):
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 0
        self.spi.mode = 0b00

    # WIP
    def get_temp(self):
        return 0

    def close(self):
        self.spi.close()