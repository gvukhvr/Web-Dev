def numbers_with_remainder(a: int, b: int, c: int, d: int):
    result = [i for i in range(a, b + 1) if i % d == c]
    if result:
        print(*result)

a, b, c, d = map(int, input().split())
numbers_with_remainder(a, b, c, d)
