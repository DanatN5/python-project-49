from brain_games.engine import engine
from brain_games.games.gcd import gcd, task
from brain_games.greeting import welcome_user


def main():
    
    name = welcome_user()

    engine(name, task, gcd)


if __name__ == "__main__":
    main()