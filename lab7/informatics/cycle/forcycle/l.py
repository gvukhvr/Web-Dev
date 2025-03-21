def sum_of_n_numbers():
    n = int(input())
    total = sum(int(input()) for _ in range(n))
    print(total)

sum_of_n_numbers()
