import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds to execute.")
        return result
    return wrapper


@log_execution_time
def greet_students():
    names = input("Enter student names separated by commas: ").split(",")
    for name in names:
        print(f"Welcome, {name.strip()}!")


greet_students()
