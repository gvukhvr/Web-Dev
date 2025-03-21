def smallest_divisor(x: int) -> int:
    for i in range(2, x + 1):
        if x % i == 0:
            return i

x = int(input())
print(smallest_divisor(x))
