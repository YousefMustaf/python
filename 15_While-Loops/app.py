# This is the syntax of the while loops:
# while consition:
#   here we wrtie the code             -- the code will be excuted as long as the conditino is right.

# for example

i = 1

while i <= 5:
    print("I love Pizza")
    i = i + 1       # if we didn't do this, we will get an infinit loop, but in case we did that, the program will start counting till it reaches 5 and then stops so we get the string "I love Pizza" five times.
print("Done")