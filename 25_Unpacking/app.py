coordinates = (1, 2, 3)

coordinates[0] * coordinates[1] * coordinates[2] # this is too long and not practicle.

# here is the practical way.
x, y, z = coordinates
# here we unpacked each item in our tuple into a variable in order.
print(x)
print(y)
print(z)