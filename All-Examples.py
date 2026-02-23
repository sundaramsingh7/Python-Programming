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


# Python Dictionary :A Python dictionary is a data structure that stores data in key-value pairs, where each key is unique and is used to retrieve its associated value. It is mainly used when you want to store and access data by a name (key) instead of by position like in a list.

#Example: This example shows how a dictionary stores data using keys and values
data = { "name": "Jake", "age": 22 }
print(data)

#Creating a Dictionary :A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:). A dictionary can also be created using the dict() function.
 
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

#Adding and Updating Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)

#Removing Dictionary Items :
#del: removes an item using its key
#pop(): removes the item with the given key and returns its value
#clear(): removes all items from the dictionary
#popitem(): removes and returns the last inserted key–value pair


d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del 
del d["age"]
print(d)

# Using pop() 
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)


#Iterating Through a Dictionary
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")


#List Comprehension in Python - It helps you write clean, readable and efficient code compared to traditional loops.
#Example : Suppose you want to square every number in a list:

a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

# For Loop vs. List Comprehension - A for loop takes multiple lines to build a new list by iterating and appending each item manually. List comprehension does same in just one line, making code shorter and easier to read.

#Using For loop
a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.append(val * 2)
print(res)

# Using List comprehension
a = [1, 2, 3, 4, 5]
res = [val * 2 for val in a]
print(res)

#Conditional Statements in List Comprehension - List comprehensions can use conditions to select or transform items based on specific rules.
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)

# ** some More example of list Comprehension **

# 1. Creating a list from a range
a = [i for i in range(10)]
print(a)

# 2. Using nested loops
c = [(x, y) for x in range(3) for y in range(3)]
print(c)

# 3. Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)


# *** Numpy Array ***
import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
res = np.array([[1, 2], [3, 4]])
print(res * 2)

# Python Arrays
import array as arr
a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# adding element to array
a.append(5)
print(a)


#Slicing of an Array 
import array as arr
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)

res = a[3:8]
print(res)

res = a[5:]
print(res)

res = a[:]
print(res)

#Reversing Elements in an Array : In order to reverse elements of an array we need to simply use reverse method.

import array
a = array.array('i', [1, 2, 3, 4, 5])

a.reverse()
print(*a)


# **** Python Sets *****

#Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates.

# 1 Creating a Set in Python
set1 = {1, 2, 3, 4}
print(set1)


# Using the set() function
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))


# Adding Elements to a Set in Python
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)

# Accessing a Set in Python
set1 = set(["Geeks", "For", "Geeks."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Geeks" in set1)

