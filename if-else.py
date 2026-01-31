#Python Conditions and If statements
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")

  #Checking if a number is positive:
  number = 15
if number > 0:
  print("The number is positive")

  #Multiple statements in an if block:

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

  #Python Elif Statement :The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Multiple Elif Statements:
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# exapmle - 2
#Day of the week checker:

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")