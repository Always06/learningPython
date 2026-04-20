## Python Numbers
# There are three numeric types in Python:
int
float
complex
# Variables of numeric types are created when you assign a value to them
## Examples:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function
## Examples:
print(type(x))
print(type(y))
print(type(z))

## Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
## Examples:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

## Float 
# Float, or "floating point number" is a number, positive or negative
# Containing one or more decimals.
## Examples:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
## Examples:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

## Complex
# Complex numbers are written with a "j" as the imaginary part:
## Examples:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

## Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
## Examples:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

## Random Number
# Python does not have a random() function to make a random number
# But Python has a built-in module called random that can be used to make random numbers
## Examples:
import random

print(random.randrange(1, 10))

## Challenge: Numbers
# Test your understanding of Python number types by completing a small coding challenge.

# Instructions
# Inside the editor, complete the following steps:
# Create a variable x and assign it the integer 5
# Create a variable y and assign it the float 3.14
# Create a variable z and assign it the complex number 2+3j
# Print the type of each variable using type()

# Create an integer
x = 5
# Create a float
y = 3.14
# Create a complex number
z = 2+3j
# Print the types
print(type(x))
print(type(y))
print(type(z))
