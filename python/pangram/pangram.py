def is_pangram(sentence):
  return set(sentence.lower()).issuperset(set('abcdefghijklmnopqrstuvwxyz'))
