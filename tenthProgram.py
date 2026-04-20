## Python Variable Exercises
# The Exercise
# The exercises are a mix of "multiple choice" and "fill in the blanks" questions.
# There are between 3 and 9 questions in each category.
# The answer can be found in the corresponding tutorial chapter.
# If you're stuck, or answer wrong, you can try again or hit the "Show Answer" button to see the correct answer.
# Find a complete collection of Python Exercises for each chapter in this tutorial in our Python Exercises page.

## Exercise: Python Variables
# What is a correct way to declare a Python variable?
x = 5

# You can declare string variables with single or double quotes.
x = "John"
# is the same as
x = 'John'
# True

# Variable names are not case-sensitive.
a = 5
# is the same as
A = 5
# False

# Select the correct functions to print the data type of a variable:
# print(type(myvar))

## Exercise: Python Variable Names
# Which is NOT a legal variable name?
# my-var = 20

# Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

# Create a variable named x and assign the value 50 to it.
x = 50

## Exercise: Python Multiple Variable Values
# What is a correct syntax to add the value 'Hello World', to 3 variables in one statement?
x = y = z = 'Hello World'

# Insert the correct syntax to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"

# Consider the following code:
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)
# What will be the result of a
# apple

## Exercise: Python Output Variable
# Consider the following code:
print('Hello', 'World')
# What will be the printed result?
# Hello World

# Consider the following code:
a = 'Hello'
b = 'World'
print(a + b)
# What will be the printed result?
# HelloWorld

# Consider the following code:
a = 4
b = 5
print(a + b)
# What will be the printed result?
# 9

# Consider the following code:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# What will be the printed result?
# Python is fantastic

# Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
  global x
  x = "fantastic"

# Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# What will be the printed result?
# Python is fantastic

## Challenge: Variables
# Instructions
# Inside the editor, complete the following steps:
# Create a variable x and assign it the value 5
# Create a variable y and assign it the value "John"
# Use the type() function to print the type of x

# Create variable x with value 5
x = 5
# Create variable y with value "John"
y = "John"
# Print the type of x
print(type(x))
