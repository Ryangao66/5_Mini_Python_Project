print("Welcome to my quiz game!")

playing = input("Do you want to play? (yes/no): ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Awesome! Let's begin!")
score = 0

answer = input("First question, which team does Michael Jordan played for?\
                 \n\tA. Utah Jazz"
                "\n\tB. Golden States"
                "\n\tC. Phoneix Sons"
                "\n\tD. Chicago Bulls"
                "\n\tAnswer: ")
if answer.lower() == "d":
    print("Awesome, that's correct!!")
    score += 1
else:
    print("That's incorrect!\nGame Over!")
    quit()

answer = input("Second question, who is NOT a character of Friends?\
                \n\tA. Joey\n\tB. Monica\n\tC. Rose\n\tD. Ross\n\tAnswer: ")
if answer.lower() == "c":
    print("Awesome, that's correct!!")
    score += 1
else:
    print("That's incorrect!\nGame Over!")

answer = input("Next question, is New Zealand a country?\
                \n\tA. Yes\n\tB. No\n\tAnswer: ")
if answer.lower() == "a":
    print("You're god damn right!!")
    score += 1
else:
    print("That's incorrect!\nGame Over!")

answer = input("First question, which team win the FIFA World Cup 2006?\
                \n\tA. Brazil"
               "\n\tB. Germany"
               "\n\tC. Italy"
               "\n\tB. France"
               "\n\tAnswer: ")
if answer.lower() == "c":
    score += 1
    print("Awesome, that's correct!! ")
else:
    print("That's incorrect!\nGame Over!")

print("You got ALL the " + str(score) + \
      " questions correct!\nAmazing can't believe you WIN a 'Million Dollars Prize'!!!!!")
print("You got " + str((score / 4) * 100) + "%.")