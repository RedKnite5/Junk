def count_rect(m: int, n: int) -> int:
  """Count the number of rectangles in an n by m grid"""

  area = m * n
  return (area * (n + m + area + 1)) // 4

def find_closest(n: int) -> int:
  end = int((2 * n - 1) ** .5) + 2  # upper bound
  
  closest = (1, 1)
  sq_dist = (n - closest[1]) ** 2
  dist = abs(n - closest[1])
  for i in range(1, end):
    for j in range(i, end):
      rects = count_rect(i, j)
      if (n - rects) ** 2 < sq_dist:
        closest = (i*j, rects)
        sq_dist = (n - rects) ** 2
        dist = abs(n - rects)
        #print(f"{i=} {j=}")
      elif (rects - n) >= n + dist:
        break
  return closest[0]

def main() -> None:
  n = find_closest(2_000_000)
  print(n)


if __name__ == "__main__":
  main()
