def my_add(*args: int) -> int:
    return sum(args)

def my_avg(*args: int) -> float:

    return sum(args) /len(args) if args else 0
   
    # if not args:
    #     return 0 
    # else:
    #    return sum(args) / len(args) # / -> float //->int

def main():
    ages = [23, 45, 22 ,43]

    print(my_add(*ages))
    print(my_avg(*ages))

    print(my_avg(23, 45, 22 ,43))


if __name__ == "__main__":
     main()

