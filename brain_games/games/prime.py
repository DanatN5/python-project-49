import random

# задание
task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    # число для задания
    number = random.randint(1, 100)
    
    expression = f'{number}'
    result = ''
    
    # счетчик делителей
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        result = 'yes'
    else:
        result = 'no'
    
    return (expression, result)