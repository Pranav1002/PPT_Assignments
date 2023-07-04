import time

def timer(func):
    def wrapper(*args, **kwargs):

        st = time.time()
        res = func(*args, **kwargs)
        
        et = time.time()
        total_time = et - st
        print(f"Execution time: {total_time:.5f} seconds")
        return res
    return wrapper

@timer
def my_function():

    time.sleep(2)

my_function()