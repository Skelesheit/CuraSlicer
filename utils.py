import sys


def cura_engine_path():
    if sys.platform == 'linux':
        return 'engines/linux/CuraEngine'
    if sys.platform == 'win32':
        return 'engines/windows/CuraEngine.exe'
