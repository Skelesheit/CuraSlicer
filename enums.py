import enum
from dataclasses import dataclass


class Quality(enum.Enum):
    DRAFT = 1
    STANDARD = 2
    SUPER = 3


class PrinterPattern(enum.Enum):
    LINEAR = 'linear'


class Printers(enum.Enum):
    CUSTOM = r'share\cura\resources\definitions\custom.def.json'
    ENDER_S1 = r'share\cura\resources\definitions\creality_ender3s1.def.json'


@dataclass
class SliceParameters:
    pattern: str = PrinterPattern.LINEAR.value
    speed_print: int = 60
    roofing_layer_count: int = 3
    count_wall_layer: int = None
    layer_height: float = None
    wall_thickness: float = None
    infill_density: float = None


@dataclass
class SliceResult:
    print_time: int = None
    volume: float = None


class Result:
    def __init__(self, output: str):
        self.data = SliceResult()
        for line in output.splitlines():
            line = line.strip()
            if "Print time" in line:
                self.data.print_time = int(line.split(" ")[-1])
            if "Filament (mm^3)" in line:
                self.data.volume = float(line.split(" ")[-1])

    @property
    def result(self):
        return self.data

    def __repr__(self):
        return (f"time to print: {self.data.print_time}\n"
                f"volume (mm^3): {self.data.volume}")

    def __str__(self):
        return self.__repr__()
