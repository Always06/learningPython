## Python Variables
# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
## Examples:
x = 5
y = "John"
print(x)
print(y)
# Variables do not need to be declared with any particular type.
# And can even change type after they have been set.
## Examples:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

## Python Casting
# If you want to specify the data type of a variable, this can be done with casting.
## Examples:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

## Python Type
# You can get the data type of a variable with the type() function.
## Examples:
x = 5
y = "John"
print(type(x))
print(type(y))

## Python Single and Double Quotes
# String variables can be declared either by using single or double quotes.
## Examples:
x = "John"
# is the same as
x = 'John'

## Python Case-Sensitive
# Variable names are case-sensitive.
## Examples:
a = 4
A = "Sally"
#A will not overwrite a
