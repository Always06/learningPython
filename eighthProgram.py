## Python Output Variables
# The print() function is often used to output variables.
## Examples:
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma
## Examples:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables
## Examples:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator
## Examples:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator
# Python will give you an error
## Examples:
x = 5
y = "John"
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas
# which even support different data types
## Examples:
x = 5
y = "John"
print(x, y)
