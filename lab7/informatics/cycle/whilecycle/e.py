def smallest_k(n: int) -> int:
    k = 0
    power = 1
    while power < n:
        power *= 2
        k += 1
    return k

N = int(input())
print(smallest_k(N))
