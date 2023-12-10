import sys
sys.path.append('src')
from user_input import UserInputHandler
from database import DatabaseController

if __name__ == "__main__":
    DatabaseController()
    inputHandler = UserInputHandler()
    inputHandler.run()