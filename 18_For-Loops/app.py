import math
# # for item in "for example python"
# #       (Punch of code)

# # for item in ("Python"):
# #     print(item)         # in this case it will return all the items in the string "Python"


# for item in ["Joe", "Dark", "Cypher", "BlindGuardian"]:
#     print(item)

# # to list out a punch of numbers without the need to write like a hundreds of numbers we use the built-in function "range"

# for item in range(20):
#     print(item)         #THIS will start countring from the index 0 to the index 19. and this is 20 numbers, this function does not print the last number as it's ends with it so it's not included in the list.

# for item in range(2, 12):
#     print(item)


# # there's another method in this function is to make the number jumbs like a steps forward like you don't want it to count like this 12345678, you want it to do it like this 1 3 5 7

# for item in range (1, 8, 2):
#     print(item)         # the last number is the steps to to jumb
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Price {total}")