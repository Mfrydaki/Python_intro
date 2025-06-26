def my_average(*numbers):

    if not numbers:
        return "No numbers provided."
    
    average =  sum(numbers) / len(numbers)
    return "{:.2f}".format(average)

def main():
    nums = [10, 20 , 30 , 40]

    ave =  my_average(*nums)
    print (ave)


if __name__ == "__main__":
    main()