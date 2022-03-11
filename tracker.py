def func_counter(func):
    counter = 0
    def count():
        func()
        counter += 1
    return count()
