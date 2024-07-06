class DataResultSlice:
    def __init__(self, output: str):
        self.time_print = None
        self.volume = None
        for line in output.splitlines():
            line = line.strip()
            if "Print time" in line:
                self.time_print = int(line.split(" ")[-1])
            if "Filament (mm^3)" in line:
                self.volume = float(line.split(" ")[-1])
        if self.time_print is None or self.volume is None:
            raise Exception("No parameters from output")

    def get_values(self):
        return self.time_print, self.volume

    def print(self):
        print("time to print: ", self.time_print,
              "volume (mm^3): ", self.volume)

    def __str__(self):
        return " time to print: " + str(self.time_print) + " volume (mm^3): " + str(self.volume)
