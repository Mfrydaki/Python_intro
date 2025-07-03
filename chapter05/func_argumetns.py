def test_arg_func(pos_arg1, pos_arg2, opt_arg1 = None, opt_arg2= None, *args, **kwargs):
    
    """
    Function to demonstrate the usage of positional, optional, additional optional(*args) and additional keyword argumentes(**kwargs).

    Params:
     pos_arg1 (Any): the first positional argument.
     pos_arg2: The second positional argument.
     opt_arg1: The first optional argument. Defaults to None.
     opt_arg2: The second option argument.Default to None.
     *args: Additional positional arguments.
     **kwargs: Additional keword arguments.
    """
    #Print positions arguments
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)

    #Print optional arguments
    print("Opt arg1: ", opt_arg1)
    print("Opt arg2:", opt_arg2)

    #Print additional pos arguments
    if args:
     print("Addiitional pos args")
     for arg in args:
        print(arg)
 
    if kwargs:
       print("Additional keyword args")
       for key, value in kwargs.items():
          print(f"{key}:{value}")

def main():
    test_arg_func("Hello", "CRF7", 100)
    print("===========")

    test_arg_func("Hello", "CF7", opt_arg2=100)
    print("===========")

    test_arg_func("Hello", "CF7", name="Panagiotis", age= 99)
    print("===========")

    test_arg_func("Hello", "CF", # pos_arg1 , pos_arg2
                100, 200, # opt_arg1, opt_arg2 
                300, "Bob" ,# *args
                name = "Panos" , street ="Coding" #**kwargs
    )



if __name__ == "__main__":
  main()