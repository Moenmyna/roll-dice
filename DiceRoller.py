import time
import random

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



dice20()