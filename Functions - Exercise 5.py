# Functions - Exercise 5 🐍

"""
import random function   
create a function `random_list_summer` creates n elemented list 
with   
min value = -100   
max value = 100
it has to print the list first and sum all the elements of it   
default element number is 15   
Don't forget to call the function  
for some features and functions you might have to search on the internet do it don't lose your courage :) 
"""


# importing random module
import random

# function definition
def random_list_summer ( n = 15 ) : # setting the default number of values that have to compose the random list ( default parameter )

    # generating a list of n random numbers between -100 and 100 using list comprehension and 'random.randint()' function
    random_list = [ random.randint ( -100, 100 ) for number in range ( n ) ]

    # Printing the randomly generated list
    print( "Generated List:", random_list )
    
    # Calculating and printing the sum of all elements in the list, for this purpose we use the built-in 'sum()' function
    list_sum = sum( random_list )
    print( "Sum of List Elements:", list_sum )

# Calling the function with the default number of elements ( 15 )
random_list_summer()    

# Calling the function with a number of elements different from the default
random_list_summer(5)   