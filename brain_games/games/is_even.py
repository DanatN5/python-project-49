import random

# задание
task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    # число для задания
    number = random.randint(0, 100)

    expression = f'{number}'
    result = ''
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    
    return (expression, result) 
