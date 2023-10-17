from functools import partial


def score(dice, category):
  return category(dice)


def score_number(target, dice):
  return sum([n for n in dice if n == target])


def score_ones(dice):
  return score_number(dice, 1)


def score_twos(dice):
  return score_number(dice, 2)


def score_threes(dice):
  return score_number(dice, 3)


def score_fours(dice):
  return score_number(dice, 4)


def score_fives(dice):
  return score_number(dice, 5)


def score_sixes(dice):
  return score_number(dice, 6)


def score_full_house(dice):
  if is_full_house(dice):
    return sum(dice)
  else:
    return 0


def score_four_of_a_kind(dice):
  if not is_four_of_a_kind(dice):
    return 0
  check_die = 0
  for d in dice:
    if check_die == d:
      return d * 4
    check_die = d


def score_little_straight(dice):
  if is_little_straight(dice):
    return 30
  else:
    return 0


def score_big_straight(dice):
  if is_big_straight(dice):
    return 30
  else:
    return 0


def score_choice(dice):
  return sum(dice)


def score_yacht(dice):
  if is_yacht(dice):
    return 50
  else:
    return 0


def count_each_die(dice):
  result = [0, 0, 0, 0, 0, 0]
  for d in dice:
    result[d - 1] += 1
  return result


def is_four_of_a_kind(dice):
  count = count_each_die(dice)
  return 4 in count or 5 in count


def is_full_house(dice):
  count = count_each_die(dice)
  return 3 in count and 2 in count


def is_yacht(dice):
  return 5 in count_each_die(dice)


def is_little_straight(dice):
  return count_each_die(dice) == [1, 1, 1, 1, 1, 0]


def is_big_straight(dice):
  return count_each_die(dice) == [0, 1, 1, 1, 1, 1]


YACHT = score_yacht
ONES = partial(score_number, 1)
TWOS = partial(score_number, 2)
THREES = partial(score_number, 3)
FOURS = partial(score_number, 4)
FIVES = partial(score_number, 5)
SIXES = partial(score_number, 6)
FULL_HOUSE = score_full_house
FOUR_OF_A_KIND = score_four_of_a_kind
LITTLE_STRAIGHT = score_little_straight
BIG_STRAIGHT = score_big_straight
CHOICE = score_choice
