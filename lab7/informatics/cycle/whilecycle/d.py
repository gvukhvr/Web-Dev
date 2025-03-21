def even_numbers(a: int, b: int):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")

a = int(input())
b = int(input())
even_numbers(a, b)
