# __      __   _      _   _                            _           
# \ \    / /__(_)__ _| |_| |_   __ ___ _ ___ _____ _ _| |_ ___ _ _ 
#  \ \/\/ / -_) / _` | ' \  _| / _/ _ \ ' \ V / -_) '_|  _/ _ \ '_|
#   \_/\_/\___|_\__, |_||_\__| \__\___/_||_\_/\___|_|  \__\___/_|  
#               |___/                                              

#  HERE IS YOUR FIRST PROGRAM BRU, JUST DO IT :)
import math
weight = int(input("Wheight: "))
weight_unit = input("(L)bs or (K)g: ").upper()
if weight_unit == "L":
    print(f"You are {math.floor(weight * 0.453592)} Kg")
elif weight_unit == "K":
    print(f"You are {math.floor(weight * 2.20462)} Lbs")
else:
    print("Please Enter a valid Unit")




# YOU ARE THE BEST, YOU'VE DONE IT SO EASY, GOOD JOB
print("Great Job")