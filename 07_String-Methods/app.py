#  ___ _       _             __  __     _   _            _    
# / __| |_ _ _(_)_ _  __ _  |  \/  |___| |_| |_  ___  __| |___
# \__ \  _| '_| | ' \/ _` | | |\/| / -_)  _| ' \/ _ \/ _` (_-<
# |___/\__|_| |_|_||_\__, | |_|  |_\___|\__|_||_\___/\__,_/__/
#                    |___/                                    

course = 'Python for beginners'

# LEN : to calculate how many characters in the string.
print(len(course))
# UPPER : transforms the entire string into upperCase.
print(course.upper())
# LOWER : the exact Opposite of the UPPER method.
print(course.lower())
# FIND : is a method that provides the index number of a specefic string.
# Normally uses the first similar letter as the result.
print(course.find('n'))
# Replace : Replaces a specefic string in the variable with another string from the user's input.
print(course.replace('beginners','Absolute Beginners'))
# This is an expresion when python checks if the specefic string in the specefic variable, and it returnes a boolean value. True, False.
print('Python' in course)   # True
print('python' in course)   # False
