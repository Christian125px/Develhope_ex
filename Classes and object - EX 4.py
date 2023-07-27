# Classes and Objects - Exercise 4 🐍

"""
Let's inherit Dog class from Animal 
add name(private) attribute to Dog class 
and then bark method to print `woof woof`

print name_of_dog 
make it bark
count the legs 
"""

# Creation of 'Animal' class
class Animal:
    
    def __init__ ( self, number_of_legs ) :
        
        self._number_of_legs = number_of_legs # making conventionally private the number_of_legs variable

        print( " Animal object was created " )

    # Creating the 'runs' method
    def runs ( self ) :
        print ( "Running started" )

    # Creating the method to count the legs `count_legs` which prints the number of legs 
    def count_legs ( self ) :
        print ( f"Number of legs - count_legs method - : {self._number_of_legs}" )

    # Creating the method to count the legs `return_legs` which returns the number of legs 
    def return_legs ( self ) :
        return self._number_of_legs
    
    # Creating another method to access '_number_of_legs' conventionally private variable
    def _another_count_legs ( self ) :
        print ( f"Number of legs - _another_count_legs method - : {self._number_of_legs}" )


# # Creating an instance / object with 4 legs from the 'Animal' class
# Lion = Animal ( 4 )
# # Calling the 'runs' method of the object we've just created
# Lion.runs()
# # Printing the number_of_legs directly from 'number_of_legs' variable of the object
# print( f"Number of legs - direct access - : {Lion._number_of_legs}" )

# # Accessing the private variable from '_another_count_legs' method
# Lion._another_count_legs()

# Creating the 'Dog' Child Class from 'Animal' Parent Class
class Dog ( Animal ) :
    
    def __init__ ( self, number_of_legs, name_of_dog ) :
        Animal.__init__ ( self, number_of_legs )
        
        self._name_of_dog = name_of_dog
    
    def bark ( self ) :
        print ( "Woof Woof" )

    def get_name ( self ):
        return self._name_of_dog
    
# Creating a dog object with 4 legs and name Kit
dog = Dog ( 4, 'Kit' )

# Printing the name of the dog by using the conventionally private variable '_name_of_dog'
print ( dog._name_of_dog )

# Printing the name of the dog by using the get_name method
print ( dog.get_name ( ) )

# Calling the bark method
dog.bark ( )

# Calling the count_legs inherited method on the dog object
dog.count_legs ( )
