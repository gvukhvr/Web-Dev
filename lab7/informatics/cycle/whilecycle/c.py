def is_power_of_two(n: int) -> str:
    return "YES" if n & (n - 1) == 0 else "NO"

N = int(input())
print(is_power_of_two(N))
