def steps(number):
  if number <= 0 or number % 1 != 0:
    raise ValueError("Only positive integers are allowed")

  steps_so_far = 0
  while number != 1:
    if is_even(number):
      number = number // 2
    else:
      number = number * 3 + 1
    steps_so_far += 1

  return steps_so_far


def is_even(n):
  return n % 2 == 0
