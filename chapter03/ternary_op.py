def compare_int(a, b):
    if a == b:
        print("Numbers are equal.")

    elif a > b :
        print("The first number is greater than the second number.")
    else:
        print("The second number is greater than the first number.")


def main():
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input. ")
        return
    
    compare_int (a, b)
    
    #1. simple ternary operator
    if a > 0:
        print("positive")
    else:
        print("non-positive")
    
    result = "positive" if a > 0 else "non-positive"
    print(result)

    #or
    print("positive" if a > 0 else "non-positive")

    #2. extented example (ternary operator)
    result = (

        print("The numbers are equal. " if a == b else 
        "The first is greater than the second ." if a > b else 
        "The second is greater than the first number. ")
        
    )

    print (result)

if __name__ == "__main__":
    main()

