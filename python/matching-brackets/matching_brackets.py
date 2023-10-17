def is_paired(input_string):
  input_list = strip_non_brackets(input_string)
  while input_list:
    if len(input_list) == 1:
      return False
    elif matching_brackets(input_list[0], input_list[1]):
      input_list.pop(0)
      input_list.pop(0)
    elif matching_brackets(input_list[0], input_list[-1]):
      input_list.pop(0)
      input_list.pop()
    else:
      return False
  return True


def strip_non_brackets(input_string):
  return list(filter(lambda c: c in '{[()]}', input_string))


def matching_brackets(c1, c2):
  if c1 == '[' and c2 == ']':
    return True
  if c1 == '{' and c2 == '}':
    return True
  if c1 == '(' and c2 == ')':
    return True
  return False
