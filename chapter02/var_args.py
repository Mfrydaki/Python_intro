def print_cities(*cities, sep=", ", end = "\n"):


    """
    Print a list of cities seperated by a specified separator and ending with a specified end char.

    Parameters:
    *cities(str): Cities which are going to be printed
    sep(str): Seperator between city name. Default is ", ".
    end(str) : End character after the last city. Default is '\n'.
    """


    if not cities:
        print ("No cities provided", end= end)
    else:
        print("Cities:", sep.join(cities), end=end)
        
    
def main():
    print_cities()
    print_cities("Chania", "Berlin")
    print_cities("Athens", "Berlin" , "Chania", sep=" | " , end=".")

if __name__ == "__main__":
    main()
