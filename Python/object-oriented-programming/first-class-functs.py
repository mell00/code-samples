#PYTHON FIRST-CLASS FUNCTIONS#

#Assign function to a variable:
def function(param):
    return param * param

variable = function(4)
print(function)
##function function at 0x101278950##
print(variable)
##16##

#Assign function to a variable, then treat variable like a function:
def function(param):
    return param * param
variable = function
print(function)
##function function at 0x101278950##
print(variable)
##function function at 0x101278950##
print(variable(4))
##16##
