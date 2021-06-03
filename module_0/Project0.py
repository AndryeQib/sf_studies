import numpy as np


def game_core_v3(number):
    """Функция получает число от 1 до 100 и пытается его отгадать"""
    first_element = 0  # задаем начальное значение
    last_element = 100  # задаем последние значение
    mean_element = (first_element + last_element) // 2  # задаем среднее значение

    count = 1
    while mean_element != number:  # сравниваем загаданное число со средним значением
        count += 1
        if number > mean_element:
            first_element = mean_element + 1  # если число больше среднего, тогда изменяем начальное значение
        else:
            last_element = mean_element - 1  # если число меньше среднего, тогда изменяем последнее значение
        mean_element = (first_element + last_element) // 2  # находим средний элемент
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []  # создаем список количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)  # формируем список случайных чисел
    for number in random_array:
        count_ls.append(game_core(number))  # передаем число и записываем число попыток отгадать его
    score = int(np.mean(count_ls))  # вычисляем среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


score_game(game_core_v3)
