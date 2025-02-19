import random

# задание
task = 'Find the greatest common divisor of given numbers.'


def gcd():
    # первое число для задания
    number1 = random.randint(0, 100)
    # второе число для задания
    number2 = random.randint(0, 100)

    expression = f'{number1} {number2}'
    result = 0

    # для использования алгоритма Евклида нужно узнать максимальное
    # и минимальное число
    max_number = max(number1, number2)
    min_nunber = min(number1, number2)
    while min_nunber > 0:
        max_number, min_nunber = min_nunber, max_number % min_nunber
        result = max_number
    return (expression, result)
