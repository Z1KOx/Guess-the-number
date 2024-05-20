from game import gameStart
from console import consoleClear, consolePause
import random


def main():
    attempts: int = 5
    TARGET_NUMBER: int = random.randint(1, 25)

    found = gameStart(attempts, TARGET_NUMBER)
    consoleClear()
    
    print(f"The target number was [{TARGET_NUMBER}]")
    
    if found:
        print("Congratulations, you guessed correctly!\n")
    else:
        print("Good luck next time!\n")

    consolePause()


# Executes our program in main function
if __name__ == "__main__":
    main()