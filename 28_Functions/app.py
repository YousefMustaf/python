# message = input ("> ")

# words = message.split(' ')
# emojis = {
#     ':)' : "😀",
#     ':(' : "😞",

# }

# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# This is how to define a function, 
#  def = define
#  the function name should be as the variable, lowreCase and using underscores

def greet_user():
    print("Hello Frind")
    print("Welcome Aboard")


print("Start")
greet_user()        # This is the correct way to call a function.
print("Finish")