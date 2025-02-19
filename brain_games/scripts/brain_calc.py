from brain_games.engine import engine
from brain_games.games.calc import task, calc
from brain_games.greeting import welcome_user


def main():
    
    name = welcome_user()

    engine(name, task, calc)


if __name__ == "__main__":
    main()