from SliceParameters import SliceParameters
from Printers import Printers
import uuid
from io import BytesIO
import subprocess
import os
from DataResultSlice import DataResultSlice


class BaseCuraEngineSlicer:

    def __init__(self, path_to_engine: str):
        self.path_to_engine = path_to_engine
        self.path_to_file = None

        self.printers_configuration = \
            {
                Printers.Ender_s1: r'share\cura\resources\definitions\creality_ender3s1.def.json',
                Printers.Custom: r'share/cura/resources/definitions/custom.def.json'
            }

    def set_file_path(self, path_to_file: str):
        if not os.path.exists(path_to_file):
            raise FileNotFoundError("File not found")
        self.path_to_file = path_to_file

    def load_file_bytes(self, byte_stream: BytesIO, extension: str):
        byte_stream.seek(0)  # Перемещение указателя в начало потока
        data = byte_stream.read()
        unique_file = uuid.uuid4()

        temp_file_path = f"{uuid.uuid4()}.{extension}"  # куда надо пихнуть наш файл?

        with open(temp_file_path, 'wb') as temp_file:
            for byte in byte_stream:
                temp_file.write(byte)
            # подойдёт ли обычный цикл?

        self.set_file_path(temp_file_path)

    def slice(self, parameters: SliceParameters, printer: Printers):
        if self.path_to_file is None:
            raise FileNotFoundError('path is not loaded')
        command = \
            [
                "slice",
                "-j", self.printers_configuration[printer],
                "-l", self.path_to_file,
                "-o", "output.gcode",
                "-s", f"speed_print={parameters.speed_print}",
                "-s", f"pattern={parameters.pattern}",
                "-s", f"roofing_layer_count={parameters.count_wall_layer}",
                "-s", f"wall_thickness={parameters.wall_thickness}",
                "-s", f"infill_density={parameters.infill_density}",
                "-s", f"quality={parameters.quality}"
            ]
        try:
            result_sub = subprocess.run(command, cwd=self.path_to_engine, capture_output=True, text=True, check=True)
            output = result_sub.stdout
            data_result = DataResultSlice(output)
            return data_result
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения команды: {e}")
            return None


class CuraEngineSlicer(BaseCuraEngineSlicer):
    def __init__(self, path_to_engine: str):
        super().__init__(path_to_engine)

    def slice(self):
        super().slice()
