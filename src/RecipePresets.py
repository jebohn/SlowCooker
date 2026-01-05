class RecipePresets:
    def __init__(self):
        # Declare presets as an empty list, intended to hold dictionaries of this form:
        # {
        #   "name": str,
        #   "times_temps": list of (time, temperature) tuples
        # }
        self.presets: list[dict[str, list[tuple[int, int]]]] = []

    def get_preset(self):
        return self.presets
    
    def add_preset(self, name, intervals):
        self.presets.append(dict["name": name, "times_temp": intervals])