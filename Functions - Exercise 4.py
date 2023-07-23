# Functions - Exercise 4 🐍

"""
Now create a fuction for John Doe and his family that greets every one in the family.   
Since it will  usually John Doe the name and surname parameter must be defaulted   
and when someone else comes it has to greet the new comer with name surname parameters which were overwritten. 
Make it possible.  
The function have to print `"Hello John Doe"` where John and Doe is parametric   
Greet each our John first then the people in the list with for loop and the function   
What you have to use
- for loop 
- function 
- string operation 
- list index

Output format 
```
Hello John Doe!
Hello Tristram Mcbride!
Hello Baldwin Preston!
Hello Wally Collins!
```
"""


# Version 1: two parameters, default values, for loop, list, string operation

# function definition
def greet ( name = 'John', surname = 'Doe' ): # assigning default values to name, surname parameters as requested

    print(f"Hello {name} {surname}!")

# creating a list containing the names of all the family members
family = [ "John Doe", "Tristram Mcbride", "Baldwin Preston", "Wally Collins" ]

# looping through all the names available in the list family
for member in family:
    name, surname = member.split() # using split method and saving name and surname of each family member into two variables ( name, surname )
    greet ( name, surname ) # call to the function for each for loop iteration


# Version 2: one parameter, for loop, list, string operation, list index

# def greet ( family ) :
#     for i in range(len(family)):
#         if i == 0:
#             print( "Hello John Doe!" )
#         else:
#             name, surname = family[i].split()
#             print( f"Hello {name} {surname}!" )

# family_list = [ "John Doe", "Tristram Mcbride", "Baldwin Preston", "Wally Collins" ]
# greet ( family_list )

