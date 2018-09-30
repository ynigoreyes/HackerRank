def MorseRepresentations(words):
    lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    transformations = set()

    for word in words:
        trans = ""
        for letter in word:
            trans += lookup[ord(letter) - 97]

        transformations.add(trans)


    return len(transformations)

