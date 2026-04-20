## Python Casting
# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. 
# This can be done with casting. Python is an object-orientated language 
# As such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal
# A float literal (by removing all decimals) 
# A string literal (providing the string represents a whole number)

# float() - constructs a float number from an integer literal
# A float literal or a string literal (providing the string represents a float or an integer)

# str() - constructs a string from a wide variety of data types
# Including strings, integer literals and float literals
## Example: 
# int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

## Examples:
# Float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

## Examples:
# String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

## Challenge: Casting
# Instructions
# Inside the editor, complete the following steps:
# Create a variable x with the integer value 1
# Convert x to a float and store it in a
# Convert x to a string and store it in b
# Print a and b

# Create an integer
x = 1
# Convert to float
a = float(x)
# Convert to string
b = str(x)
# Print values
print(a)
print(b)
