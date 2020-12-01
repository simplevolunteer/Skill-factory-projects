import numpy as np


def game_core_v2(number):
    """ Сначала устанавливаем любое random число, а потом методом деления отрезка пополам ищет загаданное число.
        Функция принимает загаданное число и возвращает число попыток """
    count = 1
    predict = np.random.randint(1, 101)
    right = 100
    left = 1
    while number != predict:
        count += 1
        if number > predict:
            right = number
            number = (left+right)//2
        elif number < predict:
            left = number
            number = (left + right)//2 + 1
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
