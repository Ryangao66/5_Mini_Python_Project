import random

top_of_range = input("Select a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please try a number greater than 0, you motherfucker!!!")
        quit()
else:
    print("Type a NUMBER!!! I have told you I am guessing a NUMBER!!!! You BIATCH!!!")
    quit()


# randrange = 1-99; randint = 1-100
# x = random.randint(1, 100)
random_number = random.randint(0, top_of_range)
guesses = 0
# print(random_number)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time!")
        continue

    if user_guess == random_number:
        print("You are god damn right!!! Lucky Bastard!!!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

print("You got it in", guesses, "guesses!" )
