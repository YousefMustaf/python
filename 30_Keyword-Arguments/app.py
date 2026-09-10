def greet_user(first_name, last_name):       
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")

greet_user("Youssef", "Mostafa") # this is a positional argummensts and from the name the position of the argument matters.

# here's an example for the keyword argument:
greet_user(last_name="Mostafa", first_name="Youssef") # this is why in the keyword argument we do not worry about the position or the argument.
# and its more practical to use keyword_argument instead of position argummetn.

calc_cost(total=50, shipping=5, discount=0.1) # this is when the keywords arguments gets very useful

