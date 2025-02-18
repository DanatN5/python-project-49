from brain_games.engine import engine
from brain_games.games.progression import TASK, progression
from brain_games.greeting import welcome_user


def main():
    
    NAME = welcome_user()

    engine(NAME, TASK, progression)


if __name__ == "__main__":
    main()