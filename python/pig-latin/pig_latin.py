VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def translate(text):
  pig_latined_words = map(translate_word, text.split(' '))
  return ' '.join(pig_latined_words)


def translate_word(text):
  first_vowel = index_of_first_vowel(text)

  # edge cases
  if text.find('xr') == 0 or text.find('yt') == 0:
    first_vowel = 0

  return text[first_vowel:] + text[:first_vowel] + "ay"


def index_of_first_vowel(text):
  index = -1
  for v in VOWELS:
    this_index = text.find(v)

    # edge cases
    if v == 'u' and text[this_index - 1] == 'q':
      continue
    if v == 'y' and this_index == 0:
      continue

    if this_index != -1 and (index == -1 or this_index < index):
      index = this_index
  return index
