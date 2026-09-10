#   ___                          _              
#  / __|___ _ __  _ __  __ _ _ _(_)___ ___ _ _  
# | (__/ _ \ '  \| '_ \/ _` | '_| (_-</ _ \ ' \ 
#  \___\___/_|_|_| .__/\__,_|_| |_/__/\___/_||_|
#                |_|                            
#   ___                     _              
#  / _ \ _ __  ___ _ _ __ _| |_ ___ _ _ ___
# | (_) | '_ \/ -_) '_/ _` |  _/ _ \ '_(_-<
#  \___/| .__/\___|_| \__,_|\__\___/_| /__/
#       |_|                                

# temp = int(input("What is the tempreture right now?\n"))

# if temp >= 30:
#     print("It's a HOT day")
# elif temp < 30 and temp > 10:
#     print("It's a GOOD day")
# else:
#     print("It's a COLD day")

name = input("Enter Your Name: \n")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name cannot be more than 50 Characters")
else:
    print("Good Name :)")

