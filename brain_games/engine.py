import prompt
from brain_games.greeting import welcome_user


def engine(TASK, game):
    name = welcome_user()
    print(TASK)
    # счетчик корректных ответов
    correct_answers = 0
    while correct_answers < 3:
        expression, result = game()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        
        if answer == str(result):
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{answer}" is wrong answer ;(.' 
                  f'Correct answer was "{result}".')
            break
        
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")