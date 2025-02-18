from brain_games.engine import engine
from brain_games.games.gcd import TASK, gcd
from brain_games.greeting import welcome_user


def main():
    
    NAME = welcome_user()

    engine(NAME, TASK, gcd)


if __name__ == "__main__":
    main()