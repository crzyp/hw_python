def func_counter(func):
    count.counter = 0
    def count(args):
        count.counter += 1
        return func(args)
    return count
