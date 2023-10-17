import math


def score(x, y):
  distance = distance_from_origin(x, y)
  if distance > 10:
    return 0
  elif distance > 5:
    return 1
  elif distance > 1:
    return 5
  else:
    return 10


def distance_from_origin(x, y):
  return math.sqrt(x * x + y * y)
