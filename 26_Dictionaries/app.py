# customer = {
#     "Name"  : "Youssef Mostafa",
#     "Email" : "youssef.teama.dev@gmail.com",
#     "Age"   : 19,
#     "birthDate": "23 October 2007"
#     "is_verified": True,
# }

# print(customer["Name"])
# print(customer.get("Name"))

# # print(customer["name"])
# print(customer.get("name"))

phone = input("Phone: ")

numbers ={
    '1' : "one",
    '2' : "two",
    '3' : "three",
    '4' : "four",
    '5' : "five"
}

output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)

