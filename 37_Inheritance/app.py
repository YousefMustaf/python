
# class Cat:
#     def walk(self):
#         print("Walk") # This without inheritince

# class Dat:
#     def walk(self):
#         print("Walk") # This without inheritince

# we simply don't wanna dublicate everything single Class we make, we just can set it to one Class and then inhert it when needed.


class Mammal: 
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk(), dog1.bark()
