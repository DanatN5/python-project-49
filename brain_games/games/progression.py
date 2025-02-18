import random

TASK = 'What number is missing in the progression?'  # задание


def progression():
    step = random.randint(1, 5)  # шаг прогрессии
    numbers_range = [i for i in range(0, 100, step)]  # диапазон чисел для прогрессии
    
    progression_start = random.randint(0, 14)  # начало прогрессии
    progression_count = random.randint(5, 12)  # количество чисел в прогрессии
    progression_stop = progression_start + progression_count  # конец прогрессии
    progression = numbers_range[progression_start:progression_stop]  # сама прогрессия

    result = random.choice(progression)
    expression = ''
    for j in progression:
        if j == result:
            expression += '.. '
        else:
            expression += str(j) + ' '
    
    return (expression.strip(), result) 
