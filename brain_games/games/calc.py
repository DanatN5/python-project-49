import random

TASK = 'What is the result of the expression?'  # задание


def calc():
    number1 = random.randint(0, 100)  # число для задания
    number2 = random.randint(0, 100)  # число для задания
    sign = random.choice(['+', '-', '*'])  # знак для задания
    expression = f'{number1} {sign} {number2}'
    result = eval(expression)
    return (expression, result)


   

    





