# Functions - Exercise 3 🐍

"""
lets see what is your user name on your computer   
to do that we are going to use os molude which is a built in module in python    
and has many built in functions in it 

to be able to use os functions   
`import os`
then call `getlogin` method of the module   
then assign the output to `user` varialbe and print the user
"""

# importing os module
import os
# calling getlogin method from os module and assigning the output to user variable
user = os.getlogin()
# printing the user
print(user)