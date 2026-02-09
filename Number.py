x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# Int : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Random Number : Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:
#Example : Import the random module, and display a random number from 1 to 9:

import random

print(random.randrange(1, 10))