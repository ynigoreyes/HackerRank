def fib(n, hashMap=None):
  # DP Solution with n being the key and the sum being the value
  if hashMap is None:
    hashMap = {}

  if n <= 1:
    return n

  elif hashMap.get(n, False):
    return hashMap[n]

  else:
    hashMap[n] = fib(n - 1, hashMap) + fib(n - 2, hashMap)

  return hashMap[n]
