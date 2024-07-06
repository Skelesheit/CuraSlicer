class SliceParameters:
    def __init__(self, speed_print: float, layer_thickness: float, layer_width: float, filling):
        self.speed_print = speed_print
        self.layer_thickness = layer_thickness
        self.layer_width = layer_width
        self.filling = filling

    def print(self):
        print("speed_print: ", self.speed_print,
              "layer_thickness: ", self.layer_thickness,
              "layer_width: ", self.layer_width,
              "filling: ", self.filling)

    def __str__(self):
        return "speed_print: " + str(self.speed_print) + " layer_thickness: " + str(
            self.layer_thickness) + " layer_width: " + str(
            self.layer_width) + " filling: " + str(self.filling)
