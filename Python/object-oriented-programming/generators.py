#PYTHON GENERATOR PATTERNS AND FUNCTIONS#

#Define a generator function:
def generator(params):
    for item in params:
        yield result_using_item

#Define an instance of a generator function:
generator_instance = generator(args)

#Create list() function to convert generator instance output into a list:
list(generator_instance)
## [list_of_results] ##

#Create a dictionary generator function:
def dict_generator(n):
    for item in xrange(n):
        dict_item = {
            'key1' : 'value1',
            'key2' : 'value2',
            'key3' : 'value3',
            'key4' : 'value4'
        }
        yield dict_item

#Create an iterator generator function:
def iterator(n):
    x = 0
    while x < n:
        yield x
        x += 1
print(iterator(4))
## 0 1 2 3 ##

#Create an even more efficient iterator generator function:
generator_instance = (result_using_item for item in [params])
list(generator_instance)
## [list_of_results] ##
