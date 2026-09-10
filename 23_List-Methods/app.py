# numbers = [5, 2, 1, 5, 8, 4]

# numbers.append(13)
# print(numbers)

# numbers.insert(0, 333)
# print(numbers)

# numbers.remove(1)
# print(numbers)

# # numbers.clear()
# # print(numbers)        this returens an empty list

# numbers.pop()
# print(numbers)

# print(numbers.index(8))
# print(50 in numbers)
# print(5 in numbers)

# print(numbers.count(5))     # This should returnes 2 since we have 2 fives in our list

# numbers.sort()     # this should sort our numbers in order from lower to higher numbers. 
# numbers.reverse
# print(numbers)

# # WE can also make a copy of our list in case we want to modify it and save a backup virsion of it like this.

# Names = ["YOUSSEF", "DARK", "MOHAMED", "AHMED", "OSAMA"]
# names_bac = Names.copy()

# Names.append("Ghareeb")
# Names.remove("DARK")
# print(Names)
# print(names_bac)


numbers = [1, 3, 8, 11, 3, 5, 8]

numbers = list(dict.fromkeys(numbers)) # This is the normal and the fastest way to remoev a dublicated item in a list
print(numbers)

# here is the tuff way.

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)