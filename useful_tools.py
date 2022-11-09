import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatless = ["John Lennon", "Paul McCarteny", "George Harison", "Ringo Star"]

def get_file_ext(filename):
  return filename[filename.index(".") + 1:]


def roll_dice(num):
  return random.randient(1, num)