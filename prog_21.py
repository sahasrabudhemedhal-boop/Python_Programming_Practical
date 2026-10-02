# Q21 Write a Python program to implement a number guessing game in which the user repeatedly enters guesses until the correct number is found. Display whether each guess is too high or too low.
correct = 50

guess = int(input("Guess the number: "))

while guess != correct:
    if guess > correct:
        print("Too High")
    else:
        print("Too Low")

    guess = int(input("Guess again: "))

print("Correct Guess!")
