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
    
    return {
        "add" :plus, 
        "subtract": minus,
        "multiply": mul,
        "division": div
    }
    

def main():
    list_of_ints = [26 , 5, 4, 5, 1, 2]

    operations = calculate(list_of_ints)

    while True:
        print('"\nChoose an operation.')
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
           choice = int(input("Please insert a number between 1 to 5:") )
        except ValueError:
            print("Invalid input.")
        
        match choice:
            case 1:
                print("Addition: ", operations["add"])
            case 2:
                print("Subtraction: ", operations["subtract"])
            case 3:
                print("Multiplication: ", operations["multiply"])
            case 4:
                print("Division: ", operations["division"])
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid input, please try again")



if __name__ == "__main__":
   main()