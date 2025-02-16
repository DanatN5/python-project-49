import random

task = 'What is the result of the expression?'


def calc():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    sign = random.choice(['+', '-', '*'])
    expression = f'{number1} {sign} {number2}'
    result = eval(expression)
    return (expression, result)


   

    





