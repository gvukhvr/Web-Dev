def sum_of_digits(x: int) -> int:
    return sum(int(digit) for digit in str(x))

x = int(input())
print(sum_of_digits(x))
