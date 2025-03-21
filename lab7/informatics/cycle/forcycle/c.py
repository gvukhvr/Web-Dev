import math

def perfect_squares_in_range(a: int, b: int):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    result = [i * i for i in range(start, end + 1)]
    if result:
        print(*result)

a, b = map(int, input().split())
perfect_squares_in_range(a, b)
