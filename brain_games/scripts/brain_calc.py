from brain_games.engine import engine
from brain_games.games.calc import TASK, calc
from brain_games.greeting import welcome_user


def main():
    
    NAME = welcome_user()

    engine(NAME, TASK, calc)


if __name__ == "__main__":
    main()