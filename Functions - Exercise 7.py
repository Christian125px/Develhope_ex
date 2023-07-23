# Functions - Exercise 7 🐍

"""
Create a lambda function that returns 2nd power of given number if it's even   
and run it on the given list   
then print the result to the screen 
"""

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# lambda function definition
even_sqare = lambda number : number ** 2 if number % 2 == 0 else number # we calculate the sqare of the number only if it is even

# list comprehension and use of the 'even_sqare' lambda function for each element of the list numbers
result_list = [ even_sqare(num) for num in numbers]

# Printing the results ( original list and list after lambda function application )
print("Original list:", numbers)
print("Result after applying the lambda function", result_list)