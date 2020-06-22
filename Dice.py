import random

def Dice():
    Roll1 = random.randint(1,6)
    Roll2 = random.randint(1,6)
    #Roll = Roll1,Roll2
    return Roll1,Roll2

for i in range(1):
    print(Dice()[0],Dice()[1])

