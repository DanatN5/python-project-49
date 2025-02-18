import random

TASK = 'Find the greatest common divisor of given numbers.'  # задание


def gcd():
    number1 = random.randint(0, 100)  # число для задания
    number2 = random.randint(0, 100)  # число для задания
    expression = f'{number1} {number2}'
    result = 0
    m = max(number1, number2)  # для использования алгоритма Евклида нужно узнать максимальное
    n = min(number1, number2)  # и минимальное число
    while n > 0:
        m, n = n, m % n
        result = m
    return (expression, result)
