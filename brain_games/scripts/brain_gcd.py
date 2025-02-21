from brain_games.engine import engine
from brain_games.games.gcd import TASK, gcd


def main():
    
    engine(TASK, gcd)


if __name__ == "__main__":
    main()