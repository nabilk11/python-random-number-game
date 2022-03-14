# Random Number Guessing Game
import quopri
import random

print("********WELCOME TO THE RANDOM NUMBER GUESSING GAME!********")

playing = input("Would you like to play? ").lower()

if playing != "yes": # if true (anything but yes, will quit game
    print("Maybe Next Time!")
    quit() 

print("Then Let's Play!")

# PICK A NUMBER + VERIFICATION
top_of_range = input("Pick a number! ")

if top_of_range.isdigit():  # isdigit() will make sure its a number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Try again with a number larger than 0 next time!")
        quit()
else:
    print("Hey, that's not a number! Pick an actual number next time!")
    quit()

random_number = random.randint(0, top_of_range) # random.randrange = random number (start, stop) not including stop
print(random_number)                       # random.randint = will include the stop point

