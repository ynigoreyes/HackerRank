# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/7/2018
# Chief Hopper

from math import ceil

def chiefHopper(arr):

    # Math: NewEnergy = 2 Energy - Height of the next building

    botEnergy = 0

    for value in reversed(arr):
        if botEnergy == value:
            botEnergy = value
        else:
            botEnergy = ceil((botEnergy + value)/2)

    return botEnergy

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = chiefHopper(arr)
    print(result)
