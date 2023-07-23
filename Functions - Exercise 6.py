# Functions - Exercise 6 🐍

"""
Implement [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) sequence as recursive function
and print first 5 elements.


ps:  
use list comprehension while creating the list
minimum element is 0 in this series
"""


def rec_fib ( n ) : # With 'n' we are passing to the function the number of elements to show from the Fibonacci sequence

    # Base case
    if n <= 1 : 
        return n
    # Recursive case
    else :
        return rec_fib ( n - 1 ) + rec_fib ( n - 2 ) # calculating the "new" number in Fibonacci sequence ( summing the previous two numbers )

# Using list comprehension for generating a list containing 'n' numbers of the Fibonacci sequence
fib_seq = [ rec_fib ( i ) for i in range(5)]
# Printing the generated list
print(fib_seq)

'''
Algorithm explained:
First execution: i = 0 -> n = 0 -> n <= 1 is True -> 0 is inserted in the list fib_seq
Second execution: i = 1 -> n = 1 -> n <= 1 is True -> 1 is inserted in the list fib_seq
Third execution: i = 2 -> n = 2 -> n <= 1 is False -> else block is executed: we sum number in position n - 1 ( 2 - 1 = 1 ) which is 1 and n - 2 ( 2 - 2 = 0 ) which is 0 and insert the resulting value ( 1 ) into the list fib_seq 
Forth execuion: i = 3 -> n = 3 -> n <= 1 is False -> else block is executed: we sum number in position n - 1 ( 3 - 1 = 2 ) which is 1 and n - 2 ( 3 - 2 = 1 ) which is 1 and insert the resulting value ( 2 ) into the list fib_seq 
Fifth execution: i = 4 -> n = 4 -> n <= 1 is False -> else block is executed: we sum number in position n - 1 ( 4 - 1 = 3 ) which is 2 and n - 2 ( 4 - 2 = 2 ) which is 1 and insert the resulting value ( 3 ) into the list fib_seq 
And so on ...
'''
# The position we refer to is the list indexing ( starting from index = 0 for the first element ) in the list fib_seq
# The value i changes according to the range function and then is passed as parameter to the Fibonacci function ( rec_fib )