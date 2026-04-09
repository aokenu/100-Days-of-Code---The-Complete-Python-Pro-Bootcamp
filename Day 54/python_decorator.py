## Python decorator function

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
#
# decorator_function(2+2)
#


import time

current_time = time.time()

# Write your code below 👇

def speed_calc_decorator(func):

    def enhanced_function():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time:.4f} seconds")
    return enhanced_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()