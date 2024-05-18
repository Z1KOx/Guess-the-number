import random # for generating random numbers
import os     # for clearing the console

def clear_console():
    # Clear the console based on the operating system
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


def play_guessing_game(tries: int, TARGET_NUMBER: int):
    print("Guess a number between 1 and 25")

    # Loop until all tries are used
    while tries:
        print(f"Your current tries [{tries}]")
        guess = int(input("Guess number: "))
        print() # Print endline after user input

        # Compare the user's guess with the target number
        if guess < TARGET_NUMBER:
            print(f"Your number {guess} is lower than the target number")
        elif guess > TARGET_NUMBER:
            print(f"Your number {guess} is higher than the target number")
        else:
            return True

        tries -= 1

    # Return False if all tries have been used up without guessing the correct number
    return False


def main():
    tries = 5
    TARGET_NUMBER = random.randint(1, 25)

    found = play_guessing_game(tries, TARGET_NUMBER)

    clear_console()
    print(f"The target number was [{TARGET_NUMBER}]")

    if found:
        print("Congratulations, you guessed correctly!\n")
    else:
        print("Good luck next time!\n")

    os.system('pause')


# Executes our program in main function
if __name__ == "__main__":
    main()