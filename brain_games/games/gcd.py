import random

task = 'Find the greatest common divisor of given numbers.'


def expression_generator():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    expression = f'{number1} {number2}'
    result = 0
    m = max(number1, number2)
    n = min(number1, number2)
    while n > 0:
        m, n = n, m % n
        result = m
    return (expression, result)
