def rotate(text, key):
  return "".join(map(lambda c: rotate_char(c, key), text))


def rotate_char(char, n):
  if not char.isalpha():
    return char
  adjusted_ord = ord(char) + n
  if (char.isupper() and adjusted_ord > 90) or (
          char.islower() and adjusted_ord > 122):
    return chr(adjusted_ord - 26)
  else:
    return chr(adjusted_ord)
