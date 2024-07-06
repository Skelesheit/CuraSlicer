from dataclasses import asdict

from engines.cura import CuraEngineSlicer
from enums import Printers, SliceParameters

parameters =  SliceParameters(
    pattern='LINEAR',
    speed_print=60,
    roofing_layer_count=3,
    count_wall_layer=2,
    layer_height=0.2,
    wall_thickness=1.2,
    infill_density=20.0
)
print(asdict(parameters))

engines = CuraEngineSlicer(r'D:\UltiMaker Cura 5.7.2\CuraEngine.exe', file_path=r'D:\STL\Cura 5.7.2.stl')
# engines.file_path = PATH
result = engines.slice(Printers.ENDER_S1.value, **asdict(parameters))
print(result)
