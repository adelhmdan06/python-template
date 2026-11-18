import time
def timer(f, *args, **kwargs):
    start_time = time.perf_counter()
    f(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

print("Time:", timer(print, "Hello"))

print("Time:", timer(zip, [1, 2, 3], [4, 5, 6]))

print("Time:", timer("Hi {name}".format, name="Bug"))