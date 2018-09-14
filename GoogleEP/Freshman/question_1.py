# Write a function to determine all the factors
# of a number. Return the factors as a list.
import math

def main():
    x = 144

    ans = []

    # Grab all the twos
    while x % 2 == 0:
        x = x / 2
        ans.append(2)

    # We only need to go up to the sqrt of x and we shoudl skip two's since we done it already
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            ans.append(i)
            x = x / i

    # if it is a really big prime number that cannot be divided by those numbers above
    if x > 2:
        ans.append(int(x))

    print(ans)

main()
