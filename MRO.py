class A:
    def __init__(self):
        print("A's constructor")

    def method(self):
        print("A's method")
class B(A):
    def __init__(self):
        super().__init__() 
        print("B's constructor")

    def method(self):
        super().method()  
        print("B's method")
class C(B):
    def __init__(self):
        super().__init__() 
        print("C's constructor")

    def method(self):
        super().method() 
        print("C's method")
a = A()
b = B()
c = C()
a.method()
b.method()
c.method()
        