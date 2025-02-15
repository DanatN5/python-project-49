import random

import prompt


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                correct_answers += 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
                break
        else:
            if answer == 'no':
                print('Correct!')
                correct_answers += 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
                break
    
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")