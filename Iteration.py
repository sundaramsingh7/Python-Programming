#Python Iterators
#An iterator is an object that contains a countable number of values.An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#which consist of the methods __iter__() and __next__().

#Example : Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Example : Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#We can also use a for loop to iterate through an iterable object:
#Example : Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

  #Example : Iterate the characters of a string:
  mystr = "banana"

for x in mystr:
  print(x)