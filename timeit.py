import time

def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        time = y - x
        print(f"Total time {time:f}")
    return wrapper()
