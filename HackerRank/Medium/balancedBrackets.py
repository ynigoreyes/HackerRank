# Complete the isBalanced function below.
def isBalanced(s):
  """
  We start with "for each character in array"

  We push to the stack if the character is a right-facing bracket
  Otherwise, we check to see if the top of the stack is the left-facing bracket's opposite
  If the stack is empty(which means we were given a left-facing bracket to start) return NO
  If the top of the stack correctly matches the opposite of the current character, pop that character
  This symolizes that we found a balanced set of brackets.
  If the stack got all of it's elements popped, then we matched all brackets, else return NO
  """


  stack = []
  for c in s:
    if c in ["{", "[", "("]:
      stack.append(c)
    elif c == "}":
      if len(stack) == 0 or stack[-1] != "{":
        return "NO"
      stack.pop()
    elif c == "]":
      if len(stack) == 0 or stack[-1] != "[":
        return "NO"
      stack.pop()
    elif c == ")":
      if len(stack) == 0 or stack[-1] != "(":
        return "NO"
      stack.pop()

  return "YES" if len(stack) == 0 else "NO"