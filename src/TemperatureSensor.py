class TemperatureSensor:
    def __init__(self, sensor):
        self.sensor = sensor        # MAX6675 instance, supplied by SlowCookerMain.py
    
    #@staticmethod
    def read_temp(self):
        print("TemperatureSensor.py: read_temp() called, calling self.sensor.get_temp()")
        curr_temp = self.sensor.get_temp()
        return curr_temp