import os
import subprocess


def consoleClear():
    """
    Clear the console screen.
    """

    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


def consolePause():
    """
    Pause the console.
    """

    if os.name == 'nt':
        subprocess.run('pause', shell=True)
    else:
        input("Press Enter to continue...")