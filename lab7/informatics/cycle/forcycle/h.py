def all_divisors(x: int):
    result = [i for i in range(1, x + 1) if x % i == 0]
    print(*result)

x = int(input())
all_divisors(x)
