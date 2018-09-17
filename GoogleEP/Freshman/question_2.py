def findFirstNonRepeating(word):
    counter = [0] * 256 # The amount of ASCII characters
    for i in word:
        counter[ord(i)] += 1

    for index, count in enumerate(counter):
        if count == 1:
            print('The first letter that does not repeat is', chr(index))
            return

findFirstNonRepeating('Hello')
