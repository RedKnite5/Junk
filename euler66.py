from itertools import count
from math import isqrt, sqrt, isclose
from fractions import Fraction


def is_square(n):
  if isinstance(n, Fraction):
    num, denom = n.as_integer_ratio()
    if denom != 1:
      return False
    n = num
  if isqrt(n)**2 == n:
    return True
  return False


def minimal_sol(D: int) -> int | None:
  # check if square
  if is_square(D):
    return None
  start = 2
  if D == 61:
    start = 1_000_000 * 352
  for x in count(start):
    if x % 1_000_000 == 0:
      print(x / 1_000_000, D)
    y_2 = Fraction(x * x - 1) / D
    if is_square(y_2):
      return x


def linear_approx(D: int, start: int) -> int:
  sqrt_D = D**.5
  for x in count(start):
    y = x * sqrt_D
    if y > 6000:
      print(y)
      exit()

    if isclose(y, round(y), abs_tol=1e-7):
      print("%.99g" % y, y == round(y))
      y_2 = Fraction(x * x - 1) / D
      if is_square(y_2):
        return x


def main() -> None:
  maximal_min = (2, 3)
  for D in range(2, 1001):
    x = linear_approx(D, 2)
    if x is None:
      continue
    if x > maximal_min[1]:
      maximal_min = (D, x)
      print("New max: ", maximal_min)

  D, x = maximal_min
  print(f"{D = } {x = }")


if __name__ == "__main__":
  main()
