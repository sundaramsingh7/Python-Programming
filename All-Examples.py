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


# Removing Elements from the Set in Python
# Using remove() Method or discard() Method , Using pop() Method , Using clear() Method

# 1. Using remove() Method or discard() Method
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)

# 2. Using pop() Method
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)


# 3.Using clear() Method
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)


# Frozen Sets in Python : A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. 
# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)


# Typecasting Objects into Sets : Typecasting objects into sets in Python refers to converting various data types into a set. Python provides the set() constructor to perform this typecasting, allowing us to convert lists, tuples and strings into sets.
# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)


# Python Tuples ;A tuple in Python is an immutable ordered collection of elements.

# Creating a Tuple
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


# Creating a Tuple with Mixed Datatypes.
tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)


#Accessing of Tuples
# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)


# Slicing of Tuple : Slicing a tuple means creating a new tuple from a subset of elements of the original tuple.
tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])


# Deleting a Tuple : Since tuples are immutable, we cannot delete individual elements of a tuple.
tup = (0, 1, 2, 3, 4)
del tup

print(tup)


# Tuple Unpacking with Asterisk (*) : In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list
tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)

#  WAP to check whether a number is even or odd by using Boolean function

def is_even(num):
    return num % 2 == 0
number = int(input("enter a number:"))

if is_even(number):
    print("the number is even")
else:
    print("the number is odd")


# *** Slicing a string

text = Python programming

substr = text [7:18]

print("Original text:",text)

print("extracted substring:",substr)

# Python programming to calculate Area of triangle


a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area of triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# To calculate the square root
# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))


# To swap two variable 
# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Without temporary variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


# Convert Kilometers to Miles
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# Convert temperature in calcius to farhenhiet
# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# # Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))




## Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)



## Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)



# # Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)




## Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)




## Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)



# Using if...elif...else
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# Using Nested if 
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
