# Syntax decorators are applied using the @ symbol placed directly above the function:
# @my_decorator
# def my_function():
#     ... function body ...
import functools


def timer_decorator(func):
    import time

    @functools.wraps(func)  # Best practice: allows function to retain its metadata, such as __name__ and __doc__
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timer_decorator
def long_running_function(exponent=6):
    print(sum(range(10**exponent)))


long_running_function(exponent=9)
