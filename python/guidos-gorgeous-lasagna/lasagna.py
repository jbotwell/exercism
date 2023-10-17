"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
  """Calculate the bake time remaining.

  :param elapsed_bake_time: int - baking time already elapsed.
  :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

  Function that takes the actual minutes the lasagna has been in the oven as
  an argument and returns how many minutes the lasagna still needs to bake
  based on the `EXPECTED_BAKE_TIME`.
  """

  return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
  """Calculate prep time based on layers preparing.

  :param number_of_layers: int - layers being prepared
  :return: int - expected time to prepare layers in minutes

  Function that estimates time to prepare lasagna based on the number of
  layers being prepared
  """

  return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  """Calculate time spent preparing lasagna so far.

  :param number_of_layers: int - layers being prepared
  :param elapsed_bake_time: int - time already in oven
  :return: int - time that has elapsed since cooking began

  Function that estimates time already spent making lasagna.
  """

  return (2 * number_of_layers) + elapsed_bake_time
