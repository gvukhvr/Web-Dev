def reverse_number(x: int) -> int:
    return int(str(x)[::-1])

x = int(input())
print(reverse_number(x))
