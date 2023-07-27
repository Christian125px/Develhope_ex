# Classes and Objects - Exercise 1 🐍

"""
Let's create Animal class and then create the 
animal object that runs and having 4 legs

create animal object with leg count 
when created print 
`"Animal object was created"`
and then call `runs` method of it and it prints 
`"Running started"`
"""

# Creation of 'Animal' class
class Animal:
    
    def __init__( self, legCount ) :
        
        self.legCount = legCount

        print( " Animal object was created " )

    # Creating the 'runs' method
    def runs ( self ) :
        print( "Running started" )

# Creating an instance / object with 4 legs from the 'Animal' class
Lion = Animal ( 4 )
# Calling the 'runs' method of the object we've just created
Lion.runs()


