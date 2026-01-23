#Tuples are used to store multiple items in a single variable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Tuple items can be of any data type:
#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")


#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
#Example - Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


