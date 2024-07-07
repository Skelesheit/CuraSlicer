import time
from dataclasses import asdict

from engines.cura import CuraEngineSlicer
from enums import Printers, SliceParameters, PrinterPattern

parameters = SliceParameters(
    pattern=PrinterPattern.LINEAR,
    speed_print=60,
    roofing_layer_count=3,
    count_wall_layer=2,
    layer_height=0.2,
    wall_thickness=1.2,
    infill_density=20.0
)

engines = CuraEngineSlicer(r'tests/models/lpwkull_2.stl', printer=Printers.ENDER_S1)
st_ = time.time()
result = engines.slice(**asdict(parameters))
print(result)
print(f'calculate: {time.time() - st_}s')
