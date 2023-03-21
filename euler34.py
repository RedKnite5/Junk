# euler34.py

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 1 and 2 dont count since theyre totals only contain 1 value and are not "sums"

max = 362880

def fact(n: int):
  if n < 0:
    raise ValueError("negative value for factorial")
  result: int = 1
  for i in range(1, n+1):
    result *= i
  return result

facts = {str(d): fact(d) for d in range(10)}

def fact_digit_sum(n: int):
  total: int = 0
  for d in str(n):
    total += facts[d]
  return total


def main():
  total = sum(n for n in range(3, max) if fact_digit_sum(n) == n)

  print(f"{total = }")

if __name__ == "__main__":
  main()

