import time

def log_calls(func):
    """
    A decorator that logs the finction call.
    """

    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    """
    A decorator that measures the excecution time of the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time= time.perf_counter()
        print(f"Excecution time of '{func.__name__}':{end_time - start_time: .7f}")
        return result
    return wrapper

#The decorators are applied bottom to top. (@measure_time: first, @log_calls: second)
#Execution is top to bottom (@log_calls : first, @measure_time:second)

@log_calls 
@measure_time 
def say_hello(name):
    time.sleep(1)
    return f"Hello {name}"


def main():
    print(say_hello("Alice"))
    print(say_hello("Mary"))

if __name__ == "__main__":
    main()
