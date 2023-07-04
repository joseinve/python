def fibonacci_d(c):
    fibonacci = 1
    f0 = 0
    f1 = 1
    for n in range(c+1):
        if n < 2:
            continue
        else:
            f0 = fibonacci
            f1 = f0-f1

            fibonacci = f0+f1
    return fibonacci
