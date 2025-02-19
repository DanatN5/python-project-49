import random

# задание
task = 'What is the result of the expression?'


def calc():
    # первое число для задания
    number1 = random.randint(0, 100)
    # второе число для задания
    number2 = random.randint(0, 100)
    # знак для задания
    sign = random.choice(['+', '-', '*'])
    
    expression = f'{number1} {sign} {number2}'
    result = eval(expression)
    return (expression, result)

   

    





