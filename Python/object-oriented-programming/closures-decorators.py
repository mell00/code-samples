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
    def function(*args):
        list=[]
        for i in args:
            print(i)
    function(your_args)













#Decorators
