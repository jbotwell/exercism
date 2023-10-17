def convert(number):
  result = ""
  if has_factor(3)(number):
    result += "Pling"
  if has_factor(5)(number):
    result += "Plang"
  if has_factor(7)(number):
    result += "Plong"
  if len(result) == 0:
    result += str(number)
  return result


def has_factor(factor):
  return lambda number: number % factor == 0
