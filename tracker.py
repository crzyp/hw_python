import functools

def func_counter(func):
    @functools.wraps(func)
    def count(*args):
        count.counter += 1
        return func(*args)
    count.counter = 0
    return count
