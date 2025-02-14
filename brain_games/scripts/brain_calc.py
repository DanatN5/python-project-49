from brain_games.greeting import welcome_user
from brain_games.calc import task
from brain_games.calc import expression_generator
from brain_games.engine import engine

def main():
    
    name = welcome_user()

    engine(name, task, expression_generator)

if __name__ == "__main__":
    main()