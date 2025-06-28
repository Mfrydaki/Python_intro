def is_square(lenght, width) -> bool:
    """
    Checks if a rectangle is a square.

    Args:
        lenght(int) : the lenght of the rectangle
        widrh(int): the width of the rectangle

    Returns:
        bool: True if the rectangle is a square, otherwise False
    """
    return lenght == width

def main():

  try:
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
  except ValueError:
    print("Invalid input. Please enter 2 ints.")
    return
  
  if is_square(length, width):
        print("The rectangle is square.")
  else:
        print("the rectangle is not square. ")

if __name__ == "__main__":
    main()