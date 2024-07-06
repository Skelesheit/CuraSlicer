import Quality


class SliceParameters:
    def __init__(self, speed_print: float, pattern: str, count_wall_layer: int, layer_height: float,
                 wall_thickness: float, infill_density: int,
                 quality: Quality):
        self.pattern = pattern
        self.speed_print = speed_print
        self.count_wall_layer = count_wall_layer
        self.layer_height = layer_height
        self.wall_thickness = wall_thickness
        self.infill_density = infill_density
        self.quality = quality

    def print(self):
        print("pattern: " + self.pattern,
              "speed print: ", self.speed_print,
              "count wall layer", self.count_wall_layer,
              "layer height: ", self.layer_height,
              "wall thickness: ", self.wall_thickness,
              "infill density: ", self.infill_density,
              "quality: ", self.quality)
