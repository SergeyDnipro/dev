import time
from functools import wraps

def time_my_func(f):
    @wraps(f)
    def wrapper(arg):
        t0 = time.time()
        return_val = f(arg)
        print(f"function {f.__name__} took {time.time() - t0}")
        return arg**2
    return wrapper

@time_my_func
def square(x):
    print('Вычисление квадрата числа: {}'.format(x))
