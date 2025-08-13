print("Welcome to the Quiz!")
score = 0

answer = input("Would you like to play the quiz? ")
print(answer)

if answer.lower() != "yes":
    quit()

answer = input("What is AI stands for? ")
if answer.lower() == "artificial intelligence":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is CNN stands for? ")
if answer.lower() == "convolutional neural network":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is LLM stands for? ")
if answer.lower() == "large language model":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is ML stands for? ")
if answer.lower() == "machine learning":
    print("correct")
    score += 1
else:
    print("Incorrect")

print("You have answered " + str(score) + " correct.")
print("You've answered " + str(score/4) + "%.")