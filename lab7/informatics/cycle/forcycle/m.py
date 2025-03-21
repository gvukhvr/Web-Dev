def count_zeros():
    n = int(input())
    zero_count = sum(1 for _ in range(n) if int(input()) == 0)
    print(zero_count)

count_zeros()
