import textwrap


def encode(plain_text):
  return split_in_fives(''.join(
      list(map(lambda c: atbash_char(c, "abcdefghijklmnopqrstuvwxyz"), plain_text))))


def decode(ciphered_text):
  return ''.join(list(map(lambda c: atbash_char(
      c, "zyxwvutsrqponmlkjihgfedcba"), ciphered_text)))


def atbash_char(char, alphabet):
  lowercased = char.lower()
  if char.isdigit():
    return char
  elif not lowercased in alphabet:
    return ''
  else:
    alphabet_position = alphabet.index(lowercased)
    return alphabet[::-1][alphabet_position]


def split_in_fives(string):
  return ' '.join(textwrap.wrap(string, 5))
