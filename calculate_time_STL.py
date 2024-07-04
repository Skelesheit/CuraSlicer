import numpy as np
from stl import mesh


def get_volume_STL(stl_file_path):
    model = mesh.Mesh.from_file(stl_file_path)
    return model.get_mass_properties()[0]


# тупейший метод расчёта
def calculate_time_STL(stl_file_path, print_speed, line_pattern):
    # Загрузка STL файла
    model_mesh = mesh.Mesh.from_file(stl_file_path)

    # Расчет объема модели
    volume = model_mesh.get_mass_properties()[0]  # Возвращает массу, объем и другие свойства

    # Примерный расчет длины линии печати (упрощенно, предполагаем, что объем связан с длиной линии)
    line_length = volume * 100  # Примерное преобразование объема в длину линии

    # Учитываем шаблон линии (зависит от плотности заполнения и других параметров)
    if line_pattern == 'linear':
        line_length *= 1
    elif line_pattern == 'grid':
        line_length *= 1.2
    elif line_pattern == 'honeycomb':
        line_length *= 1.5
    else:
        line_length *= 1  # По умолчанию

    # Расчет времени печати
    print_time = line_length / print_speed  # Время в секундах

    return print_time


# Пример использования функции
stl_file_path = 'model.stl'
print_speed = 50  # Скорость печати в мм/с
line_pattern = 'linear'

time_in_seconds = calculate_time_STL(stl_file_path, print_speed, line_pattern)
print(f"Примерное время печати: {time_in_seconds / 60:.2f} минут")
