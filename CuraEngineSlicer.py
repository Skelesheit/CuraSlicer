from SliceParameters import SliceParameters
from Printers import Printers
import uuid
from io import BytesIO


class BaseCuraEngineSlicer:
    printers_configuration = \
        {
            Printers.Ender_s1: r'share\cura\resources\definitions\creality_ender3s1.def.json',
            Printers.Custom: r'share/cura/resources/definitions/custom.def.json'
        }

    def __init__(self, path_to_engine: str):
        self.path_to_engine = path_to_engine
        self.path_to_file = None

    def set_file_path(self, path_to_file: str):
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
        pass


class CuraEngineSlicer:
    def __init__(self, path_to_engine: str):
        pass

    def slice(self):
        pass
