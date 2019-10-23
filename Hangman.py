import random
import threading
import os

words = ["penguin", "bookcase", "computer", "window", "shelf", "person", "hangman"]
word = random.choice(words)

totalGuesses = int(input("Type a number of tries: "))
usedGuesses = 0

correctGuesses = []
incorrectGuesses = []

timeUp = 0

def onTimeUp():
    print("\nTime's up!")
    os._exit(1)

timerLength = float(input("How long should the game last? (in seconds): "))

timer = threading.Timer(timerLength, onTimeUp)
timer.start()

for letter in word:
    correctGuesses.append("-")

while 1 == 1:
    print("Guesses remaining: " + str(totalGuesses - usedGuesses))
    guesses = ""
    for guess in correctGuesses:
        guesses = guesses + guess
    print(guesses)

    guesses = ""
    for guess in incorrectGuesses:
        guesses = guesses + guess
    print("Incorrect Guesses: " + guesses)

    if totalGuesses == usedGuesses:
        print("You lose.")
        raise SystemExit
    
    if timeUp == 1:
        print("Time's up!")
        break

    guess = input("Guess a letter: ")

    if timeUp == 1:
        print("Time's up!")
        break

    if guess in word:
        print("Correct guess.")
        count = 0
        for letter in word:
            if guess == letter:
                correctGuesses[count] = guess
            count += 1
    else:
        print("Incorrect guess.")
        incorrectGuesses.append(guess)
        usedGuesses += 1

    if "-" not in correctGuesses:
        print("You win!")
        break

    print("")