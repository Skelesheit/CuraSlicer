from dataclasses import asdict

from engines.cura import CuraEngineSlicer
from enums import Printers, SliceParameters


engines = CuraEngineSlicer('CURA PATH', file_path='PATH')
# engines.file_path = PATH
result = engines.slice(Printers.CUSTOM.value, **asdict(SliceParameters()))
print(result)
