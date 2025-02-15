from brain_games.greeting import welcome_user
from brain_games.is_even import is_even


def main():
    
    name = welcome_user()
    is_even(name)


if __name__ == "__main__":
    main()