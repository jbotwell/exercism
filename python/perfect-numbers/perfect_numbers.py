def classify(number):
  """ A perfect number equals the sum of its positive divisors.

  :param number: int a positive integer
  :return: str the classification of the input integer
  """
  if number <= 0 or number % 1 != 0:
    raise ValueError("Classification is only possible for positive integers.")

  sum_of_factors = sum(get_factors(number))

  if sum_of_factors == number:
    return "perfect"
  elif sum_of_factors > number:
    return "abundant"
  else:
    return "deficient"


def get_factors(number):
  factors = []
  for n in range(1, number // 2 + 1):
    if number % n == 0:
      factors.append(n)
  return factors
