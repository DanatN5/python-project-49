from brain_games.engine import engine
from brain_games.games.progression import progression, task
from brain_games.greeting import welcome_user


def main():
    
    name = welcome_user()

    engine(name, task, progression)


if __name__ == "__main__":
    main()