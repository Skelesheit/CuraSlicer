from dataclasses import asdict

from slicertools.enums import QualitySlice
from slicertools.materials import PETG
from slicertools.slicers import CuraSlicer


slicer = CuraSlicer(material=PETG())
result = slicer.slice(open('models/xyzCalibration_cube.stl', 'rb').read(), **asdict(QualitySlice.ULTRA_QUALITY))
print(result)
