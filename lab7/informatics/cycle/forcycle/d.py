def count_digit_occurrences(x: int, d: int) -> int:
    return str(x).count(str(d))

x, d = map(int, input().split())
print(count_digit_occurrences(x, d))
