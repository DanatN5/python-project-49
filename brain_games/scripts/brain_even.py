from brain_games.engine import engine
from brain_games.games.is_even import TASK, is_even
from brain_games.greeting import welcome_user


def main():
    
    NAME = welcome_user()

    engine(NAME, TASK, is_even)


if __name__ == "__main__":
    main()