def divide_nums():
    while True:
        try:
            n1 = float(input("Number 1: "))
            n2 = float(input("Number 2: "))
            result = n1 / n2
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
            continue
        else:
            print(f"The result of dividing {n1} by {n2} is {result}")
            break
        finally:
            print("Thank you for using Nicho's division program.")
divide_nums()
