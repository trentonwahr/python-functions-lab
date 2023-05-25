def sum_to(n):
  sum = 0
  for i in range(0, n + 1):
    sum = sum + i
  return sum


def largest(nums):
  largest_num = max(nums)
  return largest_num


def occurrences(string_one, string_two):
  occurs = string_one.count(string_two)
  return occurs


def product(*args):
  total = 1
  for arg in args:
    total *= arg
  return total
