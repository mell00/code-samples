#PYTHON CLOSURES AND DECORATORS#

#Closures
    #Create basic closure:
    def outer_function():
        variable = 'value'
        def inner_function():
            print(variable)
        return inner_function
    outer_function()
    ##variable##

    #:
    def outer_function():
        var = argument
        def inner_function(): #NOTE: leave parameters blank
            print(var)
        return inner_function
    instance_var = outer_function('value')
    instance_var()
    ##'value'##

    #:
    def outer_function():
        var = 'value'
        def inner_function():
            print(var)
        return inner_function
    funct_var = outer_function
    print(funct_var.__name__)
    ##'inner_function'##
    funct_var()
    ##'value'##

    #:
    def function(*args):
        list=[]
        for i in args:
            print(i)
    function(your_args)













#Decorators
    #:
    def decorator(function):
        return function
    @decorator


    #:

    def decorator(function):
        return function
    @decorator
    def function_2():
        return value

        #EQUIVALENT TO..
    decorated_funct = decorator(function_2)

    #:

    def decorator_1(function_1):
        return function_1
    def decorator_2(function_2):
        return function_2
    @decorator_1
    @decorator_2
    def wrapped_funct():
        return value

    #:
    def decorator(*args,**kwargs):
        def wrapper(function):
            return function
        return wrapper
    @decorator(params)
    def function_1:
        return value
    function_1()




    #:
