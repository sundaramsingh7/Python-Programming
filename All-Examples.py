                     # **** Additionn of two numbers ****
# Add two integer
a = 15
b = 12

# Adding two numbers
res = a + b
print(res)


# using function :
# function to add two numbers
def add(a, b):
    return a + b

# initializing numbers
a = 10
b = 5

# calling function
res = add(a,b)

print(res)


#Using Lambda Function : A lambda function is an anonymous,
#  one-line function that can perform operations without defining a full function block. It is useful for short, simple calculations.
res = lambda a, b: a + b
print(res(10, 5))

#Using operator.add : operator module provides a functionally equivalent method to the + operator.
#  This is useful when working with functional programming or reducing redundancy in complex operations.
import operator
print(operator.add(10, 5))

#Using sum() : sum() function is commonly used to add multiple numbers in an iterable like lists or tuples. It provides a simple way to add elements without using loops or explicit operators.

print(sum([10, 5]))
                      # **** Min and Max of two numbers ***** 
# min()
a = 7
b = 3
print(min(a, b))

#Using Conditional Statements : like if and else
a = 5
b = 10

if a < b:
    print(a)
else:
    print(b)


#Using Ternary Operator
a = 7
b = 2
res = a if a < b else b
print(res)

# Max()
a = 7
b = 3
print(max(a, b))

#Using if-Else statement :it is highly readable and a great choice for beginners learning control structures. 
a = 7
b = 3

if a > b:
    print(a)
else:
    print(b)


#Using sort() :In this approach, the two numbers are stored in a list, which is then sorted to find the maximum.
a = 7
b = 3

num = [a, b]
num.sort()
print(num[-1])


                             # **** Factorial of two numbers ****
#Using math.factorial() 
import math
n = 6
print(math.factorial(n))

#Using an Iterative For Loop : This method calculates factorial by manually multiplying the numbers from 1 to n inside a for loop.

n = 6
f = 1

for i in range(1, n+2):
    f *= i

print(f)

# Using a Recursive Function :This approach follows the mathematical definition of factorial by repeatedly calling the function with decreasing values until reaching the base case.

def fact(m):
    return 1 if n <= 1 else n * fact(m-1)

print(fact(7))




 