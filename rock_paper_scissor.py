import random

user_wins = 0
comp_wins = 0

options = ["rock","paper","scissor"]

while True:

    user_options = input("To play enter rock/paper/scissor or q to quit: ").lower()
    if user_options == "q":
        break

    if user_options not in options:
        continue

    random_number = random.randrange(0,2)

    computer_option = options[random_number]
    print("Computer picked", computer_option + ".")

    if user_options == "rock" and computer_option == "scissor":
        print("You won!")
        user_wins += 1

    elif user_options == "paper" and computer_option == "rock":
        print("You won!")
        user_wins += 1

    elif user_options == "scissor" and computer_option == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        comp_wins += 1

print("You won", user_wins ,"times.")
print("Computer won", comp_wins,"times.")
print("Goodbye :) ")



