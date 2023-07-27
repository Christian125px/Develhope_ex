# Classes and Objects - Exercise 3 🐍

"""
Again let's keep talking on Animal class we have.  
with 3 methods we just reached the number of legs   
to prevent direct interactin with the class variables   
most of the other programming languages have encapsulation.  
But in python we don't have it 
instead we use `_` prefix for it as convention   
it is also same for the methods   
  
`_legs` this shows us not to touch this variable its up to you 
if you want to change it you can but `_`asks you politely not to do it. 

Change the `number_of_legs` to conventional private variable 
and call from another method
"""

# Creation of 'Animal' class
class Animal:
    
    def __init__ ( self, number_of_legs ) :
        
        self._number_of_legs = number_of_legs # making conventionally private the number_of_legs variable

        print( " Animal object was created " )

    # Creating the 'runs' method
    def runs ( self ) :
        print( "Running started" )

    # Creating the method to count the legs `count_legs` which prints the number of legs 
    def count_legs ( self ) :
        print( f"Number of legs - count_legs method - : {self._number_of_legs}" )

    # Creating the method to count the legs `return_legs` which returns the number of legs 
    def return_legs ( self ) :
        return self._number_of_legs
    
    # Creating another method to access '_number_of_legs' conventionally private variable
    def _another_count_legs ( self ) :
        print( f"Number of legs - _another_count_legs method - : {self._number_of_legs}" )


# Creating an instance / object with 4 legs from the 'Animal' class
Lion = Animal ( 4 )
# Calling the 'runs' method of the object we've just created
Lion.runs()
# Printing the number_of_legs directly from 'number_of_legs' variable of the object
print( f"Number of legs - direct access - : {Lion._number_of_legs}" )

# Accessing the private variable from '_another_count_legs' method
Lion._another_count_legs()