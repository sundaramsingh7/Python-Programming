# Python Match:The match statement is used to perform different actions based on different conditions.
#nstead of writing many if..else statements, you can use the match statement.
#SyntaxGet your own Python Server
#match expression:
# case x:
 #  code block
 # case y:
#    code block
#  case z:
#    code block

#Example 1
SyntaxGet your own Python Server
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

#Example 2 :
# default value : Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


# Exapmle 3 : 
#Combined values: Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


# Example 4 : You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")