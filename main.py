import random # random.randint(1, 25)
import os     # os.system('cls')

def main():
    tries = 5
    targetNumber = random.randint(1, 25)

    while tries:
        print("Your current tries [ " + str(tries) + " ]")
        guess = int(input("Guess number: "))

        if guess < targetNumber:
            print("Your number is higher than the target number\n")
        elif guess > targetNumber:
            print("Your number is less than the target number\n")
        else:
            os.system('cls')
            print("You won the target number was [" + str(targetNumber ) + "]")
            break
    
        tries -= 1

    os.system('cls')
    print("You lost the right target number was [" + str(targetNumber ) + "]")


# start our program in main function
if __name__ == "__main__":
    main()