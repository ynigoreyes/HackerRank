def toGoatLatin(s):
    """
    :type s: str
    :rtype: str
    """
    ans = []
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    for index, word in enumerate(s.split(" ")):
        new_word = list(word)
        if new_word[0] not in vowels:
            first_letter = new_word.pop(0)
            new_word.append(first_letter)

        new_word.append('ma')
        for _ in range(index + 1):
            new_word.append("a")

        ans.append("".join(new_word))

    return " ".join(ans)
