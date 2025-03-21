def even_numbers(a: int, b: int):
    start = a if a % 2 == 0 else a + 1
    print(*range(start, b + 1, 2))

a = int(input())
b = int(input())
even_numbers(a, b)
