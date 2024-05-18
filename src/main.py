import random # For generating random numbers
import os     # For clearing the console


def clear_console():
    # Clear the console based on the operating system
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


def play_guessing_game(tries: int, TARGET_NUMBER: int) -> bool:
    print("Guess a number between 1 and 25")

    # Loop until all tries are used
    while tries:
        print(f"Your current tries [{tries}]")
        guess = int(input("Guess number: "))
        print() # Print endline after user input

        # Compare the user's guess with the target number
        if guess < TARGET_NUMBER:
            print(f"Your number {guess} is higher than the target number")
        elif guess > TARGET_NUMBER:
            print(f"Your number {guess} is lower than the target number")
        else:
            return True
    
        tries -= 1

    # Return False if all tries have been used up without guessing the correct number
    return False


def main():
    tries: int = 5
    TARGET_NUMBER: int = random.randint(1, 25)

    found = play_guessing_game(tries, TARGET_NUMBER)

    clear_console()
    print(f"The target number was [{TARGET_NUMBER}]")

    # Ternary operator
    resultPromt = "Congratulations, you guessed correctly!\n" if found else "Good luck next time!\n"
    print(resultPromt)

    os.system('pause')


# Executes our program in main function
if __name__ == "__main__":
    main()