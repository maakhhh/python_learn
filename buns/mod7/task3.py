import time
import functools
from task2 import memoize
from task1 import validate_args


def timer(func):
    @functools.wraps(func)
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.2f} секунд")
    return wrapper


@memoize
@validate_args
@timer
def fibonacci_with_memoize(n):
    if n < 2:
        return n
    return fibonacci_with_memoize(n - 1) + fibonacci_with_memoize(n - 2)


@validate_args
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(100)


