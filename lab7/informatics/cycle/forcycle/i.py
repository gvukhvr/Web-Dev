import math

def count_divisors(x: int) -> int:
    count = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            count += 1 if i == x // i else 2
    return count

x = int(input())
print(count_divisors(x))
