def is_isogram(string):
  ready_string = lower_and_strip(string)
  return len(ready_string) == len(set(ready_string))


def lower_and_strip(string):
  return ''.join([c for c in string if c.isalpha()]).lower()
