try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income / age
except ZeroDivisionError:
    print("Age Cannot be 0")
except ValueError:
    print("Invalid Value, Please Enter a Number")

# This lesson was all about handling erros instead of the error being in a long state that the end user will strugle to understand uing the try, except method we can control what does the user will see when he do an invalid action, we can control the output and the behavior of the error.