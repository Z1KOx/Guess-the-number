def getValidInput(prompt: str) -> int:
    """
    Prompt user for input and ensure it's a valid integer.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The valid integer input from the user.
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. please enter a valid number.")


def compareGuess(guess: int, TARGET_NUMBER: int) -> bool:
    """
    Compares guess with target number.

    Args:
        guess (int): The user's guess.
        TARGET_NUMBER (int): The target number to be guessed.
    
    Returns:
        bool: True if the guess is correct, otherwise False.
    """

    if guess < TARGET_NUMBER:
        print(f"Your number {guess} is lower than the target number")
    elif guess > TARGET_NUMBER:
        print(f"Your number {guess} is higher than the target number")
    else:
        return True
    
    return False


def gameStart(attempts: int, TARGET_NUMBER: int) -> bool:
    """
    Plays the guessing game where the user tries to guess a random number between 1 and 25.

    Args:
        attempts (int): The number of attempts.
        TARGET_NUMBER (int): The target number to be guessed.

    Returns:
        bool: True if the user guesses the target number correctly within the allowed attempts, otherwise False.
    """

    print("Guess a number between 1 and 25")


    while attempts:
        print(f"Your current attempts [{attempts}]")
        guess = getValidInput("Guess number: ")
        print()

        if compareGuess(guess, TARGET_NUMBER):
            return True

        attempts -= 1

    return False