class mock_thermo:
    temp = 0

    def __init__(self, initTemp):
        self.temp = initTemp

    def get_temp(self):
        return self.temp
    
    # function to increase temperature if pid is on high
    def change_temp(self, pid):
        return