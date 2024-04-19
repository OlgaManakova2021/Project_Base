def F(n):
    if n > 0:
        F(n - 2)
        print(n)
        F(n // 2)

F(4)