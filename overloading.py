class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
class MathOperations:
    def add(self, *args):
        return sum(args)    
math = MathOperations()
result1 = math.add(1, 2)
result2 = math.add(1, 2, 3)
print(result1)  
print(result2)  
