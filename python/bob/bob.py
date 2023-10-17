def response(hey_bob):
  if is_question(hey_bob) and is_yelled(hey_bob):
    return "Calm down, I know what I'm doing!"
  if is_silence(hey_bob):
    return "Fine. Be that way!"
  if is_yelled(hey_bob):
    return "Whoa, chill out!"
  if is_question(hey_bob):
    return "Sure."
  return "Whatever."


def is_question(hey_bob):
  return len(hey_bob.strip()) > 0 and hey_bob.strip()[-1] == '?'


def is_yelled(hey_bob):
  return contains_letters(hey_bob) and hey_bob == hey_bob.upper()


def is_silence(hey_bob):
  return "" == hey_bob.strip()


def contains_letters(test_string):
  return any(c.isalpha() for c in test_string)
