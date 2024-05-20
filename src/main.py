import random # For generating random numbers
import os     # For clearing the console


def clear_console():
    # Clear the console based on the operating system
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


def getValidInput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. please enter a valid number.")


def compareGuess(guess: int, TARGET_NUMBER: int) -> bool:
    if guess < TARGET_NUMBER:
        print(f"Your number {guess} is lower than the target number")
    elif guess > TARGET_NUMBER:
        print(f"Your number {guess} is higher than the target number")
    else:
        return True
    
    return False


def guessingGame(tries: int, TARGET_NUMBER: int) -> bool:
    print("Guess a number between 1 and 25")

    # Loop until all tries are used
    while tries:
        print(f"Your current tries [{tries}]")
        guess = getValidInput("Guess number: ")
        print() # Print endline after user input

        if compareGuess(guess, TARGET_NUMBER):
            return True

        tries -= 1

    # Return False if all tries have been used up without guessing the correct number
    return False


def main():
    tries: int = 5
    TARGET_NUMBER: int = random.randint(1, 25)

    found = guessingGame(tries, TARGET_NUMBER)

    clear_console()
    print(f"The target number was [{TARGET_NUMBER}]")

    # Ternary operator
    resultPrompt = "Congratulations, you guessed correctly!\n" if found else "Good luck next time!\n"
    print(resultPrompt)

    os.system('pause')


# Executes our program in main function
if __name__ == "__main__":
    main()