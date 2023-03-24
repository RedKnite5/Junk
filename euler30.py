
pow_map = {str(i): i**5 for i in range(10)}

def check_fifth_sum(n):
  return n == sum(map(pow_map.get, str(n)))

def sum_nums():
  upper_bound = pow_map["9"] * 10

  return sum(i for i in range(2, upper_bound) if check_fifth_sum(i))

def main():
  print(sum_nums())

main()