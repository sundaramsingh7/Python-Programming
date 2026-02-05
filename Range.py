#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
#This set of numbers has its own data type called range.
#Creating ranges : The range() function can be called with 1, 2, or 3 arguments, using this syntax:

#range(start, stop, step)
# Example : Create a range of numbers from 0 to 9:
x = range(10)

# range(3, 10) returns a sequence of each number from 3 to 9:
# Example : Create a range of numbers from 3 to 9:
x = range(3, 10)

#range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:

#Example : Create a range of numbers from 3 to 9:
x = range(3, 10, 2)


# Example : Convert different ranges to lists:
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

#Slicing in range
#Example : Extract a subsequence from a range:
r = range(10)
print(r[2])
print(r[:3])

# Membership Testing : Ranges support membership testing with the in operator.
#Exammple : Test if the numbers 6 and 7 are present in a range:
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

#Length : Ranges support the len() function to get the number of elements in the range.
#Example : Get the length of a range:
r = range(0, 10, 2)
print(len(r))