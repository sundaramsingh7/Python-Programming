# Class : A class in Python is a user-defined template for creating objects.
# Object : An object is a specific instance of a class. It holds its own set of data (instance variables) and can invoke methods defined by its class.
# Let's create an object from Dog class.


class Dog:
    sound = "bark"

dog1 = Dog() # Creating object from class
print(dog1.sound) # Accessing the class

# Initiate Object with __init__() : The __init__() method acts as a constructor in Python and is automatically executed when an object is created. It is used to initialize the attributes of the object with the values provided at the time of object creation.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)


