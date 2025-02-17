import random

task = 'What number is missing in the progression?'


def progression():
    step = random.randint(1, 5)  # шаг прогрессии
    numbers_range = [i for i in range(0, 100, step)]
    
    progression_start = random.randint(0, 14)
    progression_count = random.randint(5, 12)
    progression_stop = progression_start + progression_count
    progression = numbers_range[progression_start:progression_stop]

    result = random.choice(progression)
    expression = ''
    for j in progression:
        if j == result:
            expression += '.. '
        else:
            expression += str(j) + ' '
    
    return (expression.strip(), result) 
