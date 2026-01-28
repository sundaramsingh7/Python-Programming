#Python Operators
#Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:

#Example 1
print(10 + 5)

#Example 2
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# 1. Arithmetic operator
#Arithmetic operators are used with numeric values to perform common mathematical operations:

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# 2.Assignment Operators
#Assignment operators are used to assign values to variables:

count = 5
count += 2  # Equivalent to count = count + 2
print(count)
# Output: 7

message = "Hello"
message += ", World!" # Concatenation also works
print(message)
# Output: Hello, World!

# 3.Comparison Operators
#Comparison operators are used to compare two values:

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#Chaining Comparison Operators
#Python allows you to chain comparison operators:
x = 5

print(1 < x < 10)

print(1 < x and x < 10)

# 4.Logical Operators
#Logical operators are used to combine conditional statements: AND, OR, NOT
# AND
x = 5

print(x > 0 and x < 10)

#OR
x = 5

print(x < 5 or x > 10)

#NOT
x = 5

print(not(x > 3 and x < 10))





