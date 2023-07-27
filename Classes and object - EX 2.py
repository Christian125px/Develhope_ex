# Classes and Objects - Exercise 2 🐍

"""
Now continue with the Animal class we had used before 

Add a method to count the legs `count_legs`
which prints the number of legs 

Add a method to count the legs `return_legs`
which returns the number of legs 

print number of legs directly from  `number_of_legs` 
variable of the object 
"""

# Creation of 'Animal' class
class Animal:
    
    def __init__( self, number_of_legs ) :
        
        self.number_of_legs = number_of_legs

        print( " Animal object was created " )

    # Creating the 'runs' method
    def runs ( self ) :
        print( "Running started" )

    # Creating the method to count the legs `count_legs` which prints the number of legs 
    def count_legs( self ) :
        print( f"Number of legs - With count_legs method - : {self.number_of_legs}" )

    # Creating the method to count the legs `return_legs` which returns the number of legs 
    def return_legs( self ) :
        return self.number_of_legs


# Creating an instance / object with 4 legs from the 'Animal' class
Lion = Animal ( 4 )
# Calling the 'runs' method of the object we've just created
Lion.runs()
# Printing the number_of_legs directly from  `number_of_legs` variable of the object
print( f"Number of legs - direct access - : {Lion.number_of_legs}" )