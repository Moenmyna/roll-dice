import random

dice20 = random.randrange(1, 21)
roll = "You rolled a {}!"

print(roll.format(dice20))

if dice20 == 20:
    print("CRITICAL SUCCESS!")
elif dice20 == 1:
    print("CRITICAL FAIL!")