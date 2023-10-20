#!/usr/bin/env python3
# Created By: Alex M
# Date: Oct 19, 2023
# This program makes the user guess a number .
import random


def main():
    # get number from user
    computer_guess = random.randint(1, 9)
    user_guess = int(input(print(" guess a number between 1 - 9 ")))
    print("")
    if user_guess == computer_guess:
        print(" you got it right ")
    if user_guess != computer_guess:
        print("You got it wrong")


if __name__ == "__main__":
    main()
