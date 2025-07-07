def memoize(func):
    """
    A simple meoization decorator to cache results of the function.
    """

    cache = {}
    cache_stats = {"hints": 0, "misses": 0}


    def wrapper(n):
        if n in cache:
          cache_stats["hits"] +=1
          print(f"Cache hit for Fibo({n})")
        else:
            cache_stats["misses"] +=1
            print(f"Calculating Fibo({n})")
            cache [n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1: return n
    else: return fibonacci(n-1) + fibonacci(n-2)

def main():
    print([fibonacci(n) for n in range(10)])



if __name__ == "__main__":
    main()


