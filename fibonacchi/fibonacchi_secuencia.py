def fibonacci_s(c):
    fibonacci = 1
    f0 = 0
    f1 = 1
    for n in range(c+1):
        if n < 2:
            print(n)
        else:
            f0 = fibonacci
            f1 = f0-f1
            fibonacci = f0+f1
            print(fibonacci,)
