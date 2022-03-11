import time

def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print(str('Total time ' + (y - x)))
    return wrapper()
