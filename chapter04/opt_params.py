def add(a:int, b:int=20 , c:int = 30)-> int:
    return a + b + c

def full_opt_add(a:int = 0, b:int = 0, c:int=0):
    return a + b + c

def main():
    print (add(10, 20))
    print(add(100, 50))
    print(add(100, c = 40))

    print(full_opt_add(c=3, b=4, c=5))



if __name__ == "__main__":
     main()
