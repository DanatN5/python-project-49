from brain_games.engine import engine
from brain_games.games.is_even import task, is_even
from brain_games.greeting import welcome_user


def main():
    
    name = welcome_user()

    engine(name, task, is_even)


if __name__ == "__main__":
    main()