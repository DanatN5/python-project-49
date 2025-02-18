import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    NAME = prompt.string('May I have your name? ')
    print(f"Hello, {NAME}!")
    return NAME

