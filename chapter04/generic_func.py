from typing import Sequence, TypeVar, List, Any, Optional

#A generic type variable
T = TypeVar('T')

Number = TypeVar("Number", int, float)

#first()
def first(seq: Sequence[T]) -> T:
    """
    Returns the first element  of a sequence.
    If sequence is empty, raises a ValueError

    Args:
     seq(Sequence[T]): The sequence from which to get the first element.

    Returns:
     T: the first element of the sequence
    """
    if not seq:
       raise ValueError("Sequence is empty.")
    return seq[0] 

#last()
def last(seq:Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[-1]


def count_truthy(elements: List[Any]) -> int:
    """
    Counts how many elements in the list are truthy.

    Args:
      elements(List[Any]): A list of elements.
    
    Returns:
      int: The count of truthy elements in the list.
    """
    #if truthy add 1 for each element in elements
    return sum(1 for element in elements if element)



def len_str(s: Optional[str] = None) -> int:
        return len(s) if s is not None else 0

def main():
     numbers = [10, 20 , 30 , 40]

     print(f"First number: {first(numbers)})")
     print(f"Last number: {last(numbers)}")

     try:
          print("First element of []:" , first([]))
     except ValueError as e:
          print(e)

     mixed_values = [0 , True, False, "Hello", " ", None, 17]
     print("Truthy values are: ", count_truthy(mixed_values))

     print ("Length of 'Hello World': ", len_str("Hello World"))
     print ("Length 'None': ", len_str(None))

    #first element of the str
     print(first("Hello People!"))


if __name__ == "__main__":
     main()
    
