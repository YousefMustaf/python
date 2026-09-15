# class Point:
#     def __init__(self, x, y):
#        self.x = x
#        self.y = y

#     def move(self):
#         print("move")
#     def draw(self):
#         print("Draw")


# point = Point(10, 20)
# print(point.x)


# class Person:
#     def __init__(self):
#         self.name = input("Enter Your Name: ")
#         self.talk = input("Enter Your Language: ")

#     def name(self):
#         print(self.name)
#     def talk(self):
#         print(self.talk)

# person = Person()

# print(f"This Person's Name is {person.name} and he speaks in {person.talk}")

class Person:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.language = input("Enter your language: ")

    def introduce(self):
        print(f"This person's name is {self.name}.")

    def speak(self):
        print(f"He speaks {self.language}.")


person = Person()

person.introduce()
person.speak()