import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'  # задание


def is_even():
    number = random.randint(0, 100)  # число для задания
    expression = f'{number}'
    result = ''
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    
    return (expression, result) 
