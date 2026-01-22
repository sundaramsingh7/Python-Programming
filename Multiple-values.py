x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ONE VALUE TO MULTIPLE VARIABLE
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
# 1.(list)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 2.(tuple)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
