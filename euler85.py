def count_rect(m: int, n: int) -> int:
  """Count the number of rectangles in an n by m grid"""

  area = m * n
  return (area * (n + m + area + 1)) // 4


# (area * (n + m + area + 1)) // 4 = x
# n*n * (2*n + n*n + 1) = 4x
# 2*n^3 + n^4 + n^2 = 4x
# n^4 = 4x/4
# n = x^.25

def find_closest(n: int) -> int:
  start = int(n ** 0.25) - 1  # lower bound
  end = int((2 * n - 1) ** .5) + 2  # upper bound
  
  closest = (start*start, count_rect(start, start))
  sq_dist = (n - closest[1]) ** 2
  dist = abs(n - closest[1])
  for i in range(start, end):
    for j in range(i, end):
      rects = count_rect(i, j)
      if (n - rects) ** 2 < sq_dist:
        closest = (i*j, rects)
        sq_dist = (n - rects) ** 2
        dist = abs(n - rects)
        print(f"{i=} {j=}")
      elif (rects - n) >= n + dist:
        break
  return closest[0]

def main() -> None:
  n = find_closest(2_000_000)
  print(n)


if __name__ == "__main__":
  main()
