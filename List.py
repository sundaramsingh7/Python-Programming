# PYTHON LIST : Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]

# Example : 
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Example : Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# Example : Print the number of items in the list or to determine length of items:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# Example : String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# Example : What is the data type of a list?
mylist = ["apple", "banana", "cherry","Oranges"]
print(type(mylist))


# Example : Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)