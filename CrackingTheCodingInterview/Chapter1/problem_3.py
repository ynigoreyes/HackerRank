# O(n) Time
# 0(n) Space
def main(string, length):
    last_letter = length - 1    # length of the phrase
    i = len(string) - 1         # length of the final array

    # Algorithm
    # Strings are immutable so we must create an array out of it
    string = list(string)
    while last_letter != -1:
        if i = last_letter:
            # Must Break because there cannot be any more spaces
            break
        elif string[last_letter] == " ":
            # Replaces the next 3 positions with %20
            string[i] = "0"
            i -= 1
            string[i] = "2"
            i -= 1
            string[i] = "%"
        else:
            # Overwrites the furthest right position with the last letter
            string[i] = string[last_letter]
            i -= 1
            last_letter -= 1

    return "".join(string)



