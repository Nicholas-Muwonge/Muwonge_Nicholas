class Animal:
    def sound(self):
        return "Animal sound."
class Dog(Animal):
    def sound(self):
        return "The dog barks!"
class Cat(Animal):  
    def sound(self):
        return "The cat meows!"
dog = Dog()
cat = Cat()
animal = Animal()
print(animal.sound())  
print(dog.sound())  
print(cat.sound())  
