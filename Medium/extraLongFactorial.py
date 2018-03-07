# Ynigo Reyes
# Computer Science - TTU
# Class  of 2021
# 3/7/2018
# Extra Long Factorials

def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n - 1)

if __name__ == "__main__":
    n = int(input().strip())
    answer = extraLongFactorials(n)
    print(answer)