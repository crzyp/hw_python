import time

def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        total = y - x
        print(f"Total time {total:f}")
    return wrapper
