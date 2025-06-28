def compare_lists(list1, list2):
    """
    Compares two lists for the indentity and equality.

    Args:
      list1(list): the first list to compare
      list2(list): the second list to compare
    """

#identity check -> list1 is list2  
    print(f"{list1} is {list2}: {list1 is list2}")

#equality check  -> list1 == list2
    print(f"{list1} == {list2}: {list1 == list2}")

def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    #compare list
    compare_lists(my_list , your_list)
    print(id(my_list))
    print(id(your_list))


if __name__ == "__main__":
    main()