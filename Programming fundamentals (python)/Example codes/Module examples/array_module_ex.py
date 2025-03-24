from array import array
import random

# The constructor is called to create the array.
ar = array("f", [100, 3, 4, 5, 6, 8, 1, 4])

# Fill the array with random floating-point values.
for i in range(len(ar)):
    ar[i] = random.random()

# Print the values, one per line.
ar[1] = -999
ar[2] = False
ar[3] = 888.777

# Print the values, one per line.
for value in ar:
    print(value)

#ar[2] = "99.9"   # ERROR, when uncomment as array can only have homogeneous (same, similar) type value
