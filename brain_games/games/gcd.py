import random

# задание
TASK = 'Find the greatest common divisor of given numbers.'


def gcd():
    # первое число для задания
    number1 = random.randint(0, 100)
    # второе число для задания
    number2 = random.randint(0, 100)

    expression = f'{number1} {number2}'
    result = 0

    # для использования алгоритма Евклида нужно узнать максимальное
    # и минимальное число
    m = max(number1, number2)
    n = min(number1, number2)
    while n > 0:
        m, n = n, m % n
        result = m
    return (expression, result)
