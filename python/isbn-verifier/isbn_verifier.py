def is_valid(isbn):
  if not is_all_valid_chars(isbn):
    return False
  *body, check_character = isbn
  isbn_ints = ints(body, check_character)

  if len(isbn_ints) != 10:
    return False
  else:
    return digest_isbn_ints(isbn_ints) % 11 == 0


def ints(body, check_number):
  proto_result = [c for c in body if c.isdigit()]
  if check_number == 'X':
    check_number = '10'
  return proto_result + [check_number]


def digest_isbn_ints(isbn_ints):
  result = 0
  for i, n in enumerate(isbn_ints):
    result = result + (int(n) * (10 - i))
  return result


def is_all_valid_chars(isbn):
  return len(isbn) >= 10 and set(isbn).issubset(set("1234567890X-"))
