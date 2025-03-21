def perfect_squares(n: int):
    i = 1
    while i * i <= n:
        print(i * i)
        i += 1

N = int(input())
perfect_squares(N)