def factorial():
    n = int(input("enter a number: "))
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    print("factorial of", n, "is", factorial(n))
factorial()