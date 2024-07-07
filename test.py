import time
from dataclasses import asdict

from engines.cura import CuraEngineSlicer
from enums import SliceParameters, PrinterPattern

parameters = SliceParameters(
    pattern=PrinterPattern.LINEAR,
    speed_print=60,
    roofing_layer_count=3,
    count_wall_layer=2,
    layer_height=0.2,
    wall_thickness=1.2,
    infill_density=20.0
)

engines = CuraEngineSlicer(r'tests/models/lpwkull_2.stl')
result = engines.slice(**asdict(parameters))