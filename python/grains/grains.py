def square(number):
  if number < 1 or number > 64:
    raise ValueError("square must be between 1 and 64")
  else:
    return 2**(number - 1)


def total():
  big = 0
  for n in range(1, 65):
    big += square(n)
  return big
