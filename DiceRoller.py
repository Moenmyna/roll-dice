import time
import random
import re

roll = "You rolled a {}!"

def dice20():
    d20 = random.randrange(1, 21)
    print("Rolling...")
    time.sleep(0.5)
    
    global roll
    print(roll.format(d20))
    if dice20 == 20:
        print("CRITICAL SUCCESS!")
    elif dice20 == 1:
        print("CRITICAL FAIL!")

def dice4():
    d4 = random.randrange(1, 5)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d4))

def dice6():
    d6 = random.randrange(1, 7)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d6))

def dice8():
    d8 = random.randrange(1, 9)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d8))

def dice10():
    d10 = random.randrange(1, 11)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d10))

def dice12():
    d12 = random.randrange(1, 13)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d12))

def dice100():
    d100 = random.randrange(1, 101)
    print("Rolling...")
    time.sleep(0.5)

    global roll
    print(roll.format(d100))

def Choice():

    print("1) d4")
    print("2) d6")
    print("3) d8")
    print("4) d10")
    print("5) d%")
    print("6) d12")
    print("7) d20")
    
    while True:
        try:
            userChoice = int(input("Please choose a dice to roll."))
            break
        except:
            print("Please choose from the available options.")

    if userChoice == 1:
        dice4()
    elif userChoice == 2:
        dice6()
    elif userChoice == 3:
        dice8()
    elif userChoice == 4:
        dice10()
    elif userChoice == 5:
        dice100()
    elif userChoice == 6:
        dice12()
    elif userChoice == 7:
        dice20()
    else:
        print("Please choose from the available options.")

Choice()