import functools 

def calculate(args):
    def plus():
        """ Return the sum of the numbers """
        return functools.reduce(lambda x, y : x+y , args)
    
    def minus():
        return functools.reduce(lambda x, y : x - y, args)
    
    #[100, 10, 20, 30 ] -> 100 -10 -20 -30
    def mul():
        return functools.reduce(lambda x, y : x *y, args)
    
    def div():
        #if not 0 in args[1:]:...
        return args[0] / sum(args[1:])
    
    return plus, minus, mul, div
    

def main():
    list_of_ints = [26 , 5, 4, 5, 1, 2]

    plus_func, minus_func, mul_func, div_func = calculate(list_of_ints)

    print(f"plus func: {plus_func()}")
    print(f"minus func: {minus_func()}")
    print(f"mul func: {mul_func()}")
    print(f"div func: {div_func()}")


if __name__ == "__main__":
   main()