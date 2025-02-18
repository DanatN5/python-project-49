from brain_games.engine import engine
from brain_games.games.prime import TASK, prime
from brain_games.greeting import welcome_user


def main():
    
    NAME = welcome_user()

    engine(NAME, TASK, prime)


if __name__ == "__main__":
    main()