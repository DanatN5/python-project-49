from brain_games.engine import engine
from brain_games.games.prime import prime, task
from brain_games.greeting import welcome_user


def main():
    
    name = welcome_user()

    engine(name, task, prime)


if __name__ == "__main__":
    main()