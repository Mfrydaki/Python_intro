def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000 )-> str:

    """
    Returns a string representing a date in the format "dd/mm/yy"

    Args: 
    day(int) : the day of the month Defaults to 1.
    month(int): the month of the year. Defaults to 1.
    year(int) : the year. Defaults to 2000

    """

    return(f"{day:02d}/{month:02d}/{year:4d}")

def main():
    print(get_formatted_date()) #01/01/2000
    print(get_formatted_date(10)) #10/01/2000
    print(get_formatted_date(14, 2)) #14/02/2000
    print(get_formatted_date(14, 2 , 2025)) #14/02/2025

    #01/01/2025
    print(get_formatted_date(year = 2025))
    




if __name__ == "__main__":
  main()
