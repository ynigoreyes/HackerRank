class Solution:
  def maskPII(self, S):
    """
    :type S: str
    :rtype: str
    """

    state = "email" if S[1].isalpha() == True else "number"
    answer = []

    if state == "email":
      answer = S[0].lower() + "*****"
      seen_at = False
      for i, char in enumerate(S):
        if char == "@":
          answer = answer + S[i - 1].lower() + char
          seen_at = True

        elif seen_at == True:
          answer += char.lower()

      return answer

    elif state == "number":

      answer = []
      star = False

      section_count = 0
      char_count = 1

      for i in range(len(S) - 1, -1, -1):

        print("On count {} and char {}".format(char_count, S[i]))

        if char_count == 5 and S[i].isdigit():
          star = True
          answer.insert(0, "-")
          answer.insert(0, "*")
          char_count = 1

        # First 4 numbers
        elif star == False and S[i].isdigit():
          answer.insert(0, S[i])

        # The 3 number sections
        elif star and S[i].isdigit():
          answer.insert(0, "*")
          if char_count == 3:
            answer.insert(0, "-")
            char_count = 0

        else:
          continue

        char_count += 1

      # adds the plus at the end if there is an area code
      if len(answer) == 17 or len(answer) == 13:
        answer.pop(0)
        if len(answer) == 16:
          answer.insert(0, "+")

      elif len(answer) > 11:
        answer.insert(0, "+")

      return "".join(answer)
