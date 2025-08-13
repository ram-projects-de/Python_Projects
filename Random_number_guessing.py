import random

number_range = input("Enter a number: ")

if number_range.isdigit():
    number_range = int(number_range)

    if number_range <= 0:
        print("Enter a number greater than 0 next time.")
        quit()

else:
    print("Enter a number next time")
    quit()

random_number = random.randrange(0, number_range)
guesses = 0

while True:
    guesses += 1

    user_guess = input("Guess the number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter a number next time")

    if user_guess == random_number:
        print("Hooray! You got it")
        break

    elif user_guess > random_number:
        print("Awww so close, the number you guessed is above my number")

    else:
        print("Awww so close, the number you guessed is below my number")


print("You got it in", guesses, "guesses")
if guesses <= 5:
    print("You're a wizard")

elif 6 <= guesses <= 10:
    print("You're a champion")

else:
    print("Congratulations")