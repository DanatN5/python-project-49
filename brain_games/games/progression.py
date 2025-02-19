import random

# задание
task = 'What number is missing in the progression?'


def progression():
    # шаг прогрессии
    step = random.randint(1, 5)
    # диапазон чисел для прогрессии
    numbers_range = [i for i in range(0, 100, step)]
    # начало прогрессии
    progression_start = random.randint(0, 14)
    # количество чисел в прогрессии
    progression_count = random.randint(5, 12)
    # конец прогрессии
    progression_stop = progression_start + progression_count
    # сама прогрессия
    progression = numbers_range[progression_start:progression_stop]

    result = random.choice(progression)
    expression = ''
    for j in progression:
        if j == result:
            expression += '.. '
        else:
            expression += str(j) + ' '
    
    return (expression.strip(), result) 
