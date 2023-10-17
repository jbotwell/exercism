def is_armstrong_number(orig_number):
  total = 0
  num_digits = get_num_digits(orig_number)
  for n in digits_gen(orig_number):
    total += n ** num_digits
  return total == orig_number


def get_num_digits(n):
  result = 0
  while n > 0:
    result += 1
    n = n // 10
  return result


def digits_gen(n):
  while n > 0:
    yield n % 10
    n = n // 10
