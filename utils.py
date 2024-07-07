import sys

import trimesh
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def cura_engine_path():
    if sys.platform == 'linux':
        return str(BASE_DIR / 'engines/linux/CuraEngine')
    if sys.platform == 'win32':
        return str(BASE_DIR / 'engines/windows/CuraEngine.exe')


def file3d_to_stl(file_path):
    mesh = trimesh.load(file_path)
    output_name = file_path.rsplit('.', 1)[0] + ".stl"
    mesh.export(output_name)
    return output_name
