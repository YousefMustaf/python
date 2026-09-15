import converters
import utils
from converters import kg_to_lbs

    
numbers = [10, 11, 17, 89, 124]    

print(utils.find_max(numbers))

print(kg_to_lbs(100))
print(converters.kg_to_lbs(100))


# weight = input("Enter Your Weight: ")
# unit = input("Select The Weight Unit\n(KG) or (LBS): ").upper


# if unit == "KG":
#     print(f"Your Weigh Is {converters.kg_to_lbs(weight)}")
# elif unit == "LBS":
#     print(f"Your Weigh Is {converters.lbs_to_kg(weight)}")

