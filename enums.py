import enum
from dataclasses import dataclass


class Quality:
    DRAFT = 1
    STANDARD = 2
    SUPER = 3


class PrinterPattern:
    LINEAR = 'linear'


class Printers:
    CUSTOM = r'definitions\custom.def.json'
    ENDER_S1 = r'definitions\creality_ender3s1pro.def.json'  #r'C:\Users\sasha\PycharmProjects\CuraSlicer\'


@dataclass
class SliceParameters:
    pattern: str = PrinterPattern.LINEAR
    speed_print: int = 60
    roofing_layer_count: int = 3
    count_wall_layer: int = None
    layer_height: float = None
    wall_thickness: float = None
    infill_density: float = None
    center_object: bool = True
    rotate_model: int = 0
    bed_size: str = '9999,9999'
    auto_position: bool = True


@dataclass
class SliceResult:
    print_time: int = None
    volume: float = None


class Result:
    def __init__(self, output: str):
        self.data = SliceResult()
        for line in output.splitlines()[::-1]:
            line = line.strip()
            if "Print time (s)" in line:
                self.data.print_time = int(line.split(" ")[-1])
            elif "Filament (mm^3)" in line:
                self.data.volume = float(line.split(" ")[-1])
            if None not in [self.data.print_time, self.data.volume]:
                return

    @property
    def result(self):
        return self.data

    def __repr__(self):
        return (f"time to print: {self.data.print_time}\n"
                f"volume (mm^3): {self.data.volume}")

    def __str__(self):
        return self.__repr__()
