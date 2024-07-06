import logging
import os
import subprocess

from enums import Result


class CuraEngineSlicer:

    def __init__(self, engine_path: str, file_path):
        self._engine_path = engine_path
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")
        self._file_path = path

    def slice(self, printer: str, **parameters) -> Result:
        assert self.file_path is not None, FileNotFoundError('File not loaded')

        try:
            result_sub = subprocess.run(self.command(printer, **parameters), cwd=self._engine_path,
                                        capture_output=True, text=True, check=True)
            return Result(result_sub.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Ошибка выполнения команды: {e}")
            raise

    def command(self, printer: str, **parameters):
        return [
                "slice",
                "-j", printer,
                "-l", self.file_path,
            ] + [f"-s {key}=value" for key, value in parameters if value is not None]
