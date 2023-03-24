from itertools import product

def distinct_powers(n):
  return len({i**j for i, j in product(range(2, n+1), range(2, n+1))})

def main():
  print(distinct_powers(100))

main()