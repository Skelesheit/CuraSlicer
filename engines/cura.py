import logging
import os
import subprocess
from utils import cura_engine_path
from enums import Result


class CuraEngineSlicer:

    def __init__(self, file=None, printer=None, engine_path: str = None, **slice_params):
        if engine_path is None:
            engine_path = cura_engine_path()
        self.printer = printer
        self._engine_path = engine_path
        self._file_path = file
        self.slice_params = slice_params or None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")
        self._file_path = path

    def slice(self, file=None, gcode_path: str = 'o.gcode', **parameters) -> Result:
        if file is not None:
            self.file_path = file
        assert self.file_path is not None, FileNotFoundError('File not loaded')
        self._gcode_path = gcode_path

        if not parameters:
            parameters = self.slice_params
        slice_ = subprocess.Popen(self.command(**parameters), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = slice_.communicate()
        return Result(stdout)

    def command(self, **parameters):
        return " ".join([
                            self._engine_path,
                            "slice",
                            "-o", self._gcode_path,
                            "-j", self.printer,
                            "-l", self.file_path,
                        ] + [f"-s {key}={value}" for key, value in parameters.items() if value is not None])
