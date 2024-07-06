import subprocess
import os


def get_STL_time_from_cura(engine_path: str, stl_file_path: str, config_printer_path: str, print_speed: int,
                           line_pattern: str, count_wall_layer: int):
    exename = 'CuraEngine.exe'
    all_path = engine_path + '\\' + exename
    if not os.path.exists(all_path):
        raise FileNotFoundError(all_path)
    command = [
        all_path,
        "slice",
        "-j", config_printer_path,  # Файл конфигурации принтера
        "-l", stl_file_path,
        "-s", f"speed_print={print_speed}",
        "-s", f"pattern={line_pattern}",
        "-s", f"roofing_layer_count={count_wall_layer}",  # Указываем количество стенок
        "-o", "output.gcode"
    ]

    # Запуск CuraEngine и получение вывода
    try:
        result = subprocess.run(command, cwd=engine_path, capture_output=True, text=True, check=True)
        output = result.stdout

        # Поиск времени печати в выводе
        time_in_seconds = None
        for line in output.split('\n'):
            print(line)
            if "Print time" in line:
                print(line)
                time_str = line.split(" ")[-1]
                return int(time_str)
        return time_in_seconds

    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e}")
        return None


# Пример использования функции
print_speed = 60  # Скорость печати в мм/с
line_pattern = 'linear'
count_wall_layer = 3

engine_path = r'D:\UltiMaker Cura 5.7.2'
config_printer_path = r'share\cura\resources\definitions\creality_ender3s1.def.json'
path_to_STL = r'D:\STL\xyzCalibration_cube.stl'

time_in_seconds = get_STL_time_from_cura(engine_path, path_to_STL, config_printer_path, print_speed, line_pattern,
                                         count_wall_layer)
if time_in_seconds is not None:
    print(f"Примерное время печати: {time_in_seconds / 60:.2f} минут")
else:
    print("Не удалось определить время печати")
