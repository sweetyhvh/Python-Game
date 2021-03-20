#Imports 
import random, time

#Vars
you_take_the_stick = False
random_rat = random.randint(1, 100)

#Game
first = input("""
----------------------------
[A] - Door half open
[B] - Vent
----------------------------\n""")

if first ==  "A":
    print("You meet Alfred! (For some reason he has a Viking hat)")
    Tormar = input("You don't have much time... You have 2 options: [D] - Pretend to be asleep. [C] - Run away\n")
    if Tormar == "D":
        print("You died")
        exit()
    if Tormar == "C":
        print("You won.")
        exit()

if first == "B":
    print("You're stinky and the water comes up to your knees. You walk for half an hour and you find a dry and light area.")
    stick = input("You found a big stick. Do you take it? [Y] Yes, [N] No\n")
    if stick == "Y":
        you_take_the_stick = True
    elif stick == "N":
        print("You diden't take the stick")
    else:
        print("You diden't choose anything, You die")
        exit()
    print("You go ahead and you find a Rat wearing a kimono. The rat asks you: How much is 13 * {}?".format(random_rat))
    Beginning = time.time()
    option = int(input("What's the result? "))
    final = time.time()
    if final - Beginning >= 20:
        print("You died because you're slow")
        exit()
    if option == 13 * random_rat:
        print("You died. Rats hate smart people.\n Game Over")
    else:
        print("The rat opens a door for you, you goes down a hall and tunnel collapses, you no longer have an exit, you see a kind of vent but it is far away.")

        option = input("[W] - Wait for someone to rescue you | [T] - Try to exit\n")

        if option == "W":
            print("An alligator appears and eats you.\nGame Over")
        elif option == "T" and you_take_the_stick:
            print("You use the stick you picked up earlier to propel yourself and get out of the maze.\n You won, ez")
        else:
            print("Choose a valid option, you died")
