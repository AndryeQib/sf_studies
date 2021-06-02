import numpy as np


def game_core_v3(number):
    min_element = 0
    max_element = 100
    mean_element = (min_element + max_element) // 2

    count = 1
    predict = np.random.randint(1, 101)
    while mean_element != predict:
        count += 1
        if predict > mean_element:
            min_element = mean_element + 1
        else:
            max_element = mean_element - 1
        mean_element = (min_element + max_element) // 2
    return count


def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


score_game(game_core_v3)
