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

#Create built-in map() function, using the function created above:
map_var = map(function,args)
print(map_var)
##[1,4,9,16,25]##

#Create custom map() function (custom_map), using the function created above:
def custom_map(function,params):
    result = []
    for item in params:
        result.append(function(item))
    return result

var = custom_map(function,[1,2,3,4,5])
print(var)
##[1,4,9,16,25]##

#Pass in an alternate function into the custom map() function (custom_map):
def function_2(param):
    return param * param * param
def custom_map(function,params):
    result = []
    for item in params:
        result.append(function(item))
    return result

var_2 = custom_map(function_2,[1,2,3,4,5])
print(var_2)
##[1,8,27,64,125]##
