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


#__str__() Method : __str__ method in Python allows us to define a custom string representation of an object
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)


# Class Variables : These are variables that are shared across all instances of a class. It is defined at class level, outside any methods. All objects of class share same value for a class variable unless explicitly overridden in an object.

# Instance Variables : Variables that are unique to each instance (object) of a class. These are defined within __init__() method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)


# Conditional statments 
# if condition
age = 20
if age >= 18:
    print("Eligible to vote.")


# if-else condition
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")