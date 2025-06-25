items = [1, 3, 3.14 , True, "HELLO"]

for item in items:
    print(item, end = " ")
print()

nest_list = [
    [1, 3],
    [3 ,4],
    [5, 6]
]
#nest_list = [[1,3], [3,4], [5,6]]
print(f"first list item: {nest_list[0]}")

#i want to get the "3"
print (nest_list[1],[0])

#[3,4] [1,3]
print(nest_list[1], nest_list[0], sep=" ,")