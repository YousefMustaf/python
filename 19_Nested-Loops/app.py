# This program uses two loops: the outer loop runs 4 times,
# and for each of those times the inner loop runs 3 times.
# So it prints every combination of x and y from 0 to 3 and 0 to 2.
# Example: (0, 0), (0, 1), (0, 2), then (1, 0), (1, 1), ...
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# peoples = ["Youssef", "Osama", "Ahmed", "Gharib"]

# skills = ["Html", "Css", "JS"]

# for name in peoples :   # OUTER LOOP
#     print(f"{name} Siills is: ")

#     for skill in skills:

#         print(f" - {skill}")

peoples = {

    "Youssef" :{
        "Html" : "70%",
        "CSS" : "80%",
        "JS" : "70%"
    },

    "Osama" : {
        "Html" : "90%",
        "CSS" : "80%",
        "JS" : "90%"
    },

    "Ahmed" : {
        "Html" : "70%",
        "CSS" : "60%",
        "JS" : "90%"
    }
}

# print(peoples["Osama"])
# print(peoples["Osama"]["CSS"])

# for name in peoples:

#     print(f"Skills and progress for {name} Is: ")

#     for skill in peoples[name]:
#         print(f"{skill.upper()} => {peoples[name][skill]}")

numbers = [2, 2, 2, 2, 7]

# for number in numbers:
#     print(f"X" * number)

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "X"
    print(output)
