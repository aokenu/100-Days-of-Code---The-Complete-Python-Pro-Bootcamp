## Python decorator function

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function

decorator_function(2+2)