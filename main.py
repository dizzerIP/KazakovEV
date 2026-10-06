import math
import logging
import sys

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("logs/file_txt.log", encoding="utf-8") # Настройка логирования в файл
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

def get_triangle_info(s1, s2, s3):
    logging.info("Начало запроса")
    logging.debug(f"Параметры запроса: s1='{s1}', s2='{s2}', s3='{s3}'")
    try:
        a = float(s1)
        b = float(s2)
        c = float(s3)

    except ValueError as e:
        logging.error(f"Ошибка входных данных: {e}")
        return "Ошибка", [(-2, -2), (-2, -2), (-2, -2)]

    if a + b <= c or a + c <= b or b + c <= a:
        logging.warning(f"Треугольник не существует")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if round(a, 2) == round(b, 2) == round(c, 2):
        t_type = "равносторонний"
    elif a == b or b == c or a == c:
        t_type = "равнобедренный"
    else:
        t_type = "разносторонний"
    logging.info(f"Тип треугольника: {t_type}")

    sides = sorted([a, b, c])
    base, side1, side2 = sides[2], sides[0], sides[1]

    margin_x = max(0, (100 - base) / 2)
    A = (int(margin_x), 100)
    B = (int(margin_x + base), 100)

    p = (base ** 2 + side1 ** 2 - side2 ** 2) / (2 * base)
    h = math.sqrt(max(0, side1 ** 2 - p ** 2))

    C = (int(margin_x + p), int(100 - h))

    logging.debug(f"Вычисленные координаты: A={A}, B={B}, C={C}")
    logging.info("Запрос обработан")

    return t_type, [A, B, C]


if __name__ == "__main__":
    print("Введите 3 стороны (каждую с новой строки):")
    line1 = input()
    line2 = input()
    line3 = input()

    res_type, res_coords = get_triangle_info(line1, line2, line3)

    print(f"Тип: {res_type}")
    print(f"Координаты: {res_coords}")