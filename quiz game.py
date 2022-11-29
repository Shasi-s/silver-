print("Welcome to my Harry Potter relic quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the relic of house Ravenclaw? ")
if answer.lower() == "ravenclaw's diadem":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the relic of house Hufflepuff? ")
if answer.lower() == "hufflepuff's cup":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the relic of house Slytherin? ")
if answer.lower() == "slytherin's locket":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" What is the relic of house Griffindor?")
if answer.lower() == "griffindor's sword":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")