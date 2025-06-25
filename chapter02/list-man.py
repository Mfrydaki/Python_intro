fruits = ["Apple", "Banana", "Cherry"]
print(f"Initial list: {fruits}")

#Add a fruit at the end of the list
fruits.append("Berry")
print("After adding Berry: ",fruits)

#Add two fruits at the list
fruits.extend(["Grapes" , "Fig"])
print("After adding Grapes and Fig: ",fruits)

#Insert an element in a specific position
fruits.insert(1, "Coconut")
print ("After adding Coconut: " ,fruits)

#Update the first element
fruits[0] = "Watermelon"
print ("After updating the first element: " ,fruits)

#Update a slice of list(two elements)
fruits[1:3] = ["A" , "C"]
print ("After slicing: " ,fruits)

#pop()
removed_item = fruits.pop()
print(f"Removed item: {removed_item}")
print ("After pop(): " ,fruits)

#remove
fruits.remove("C")
print ("After remove('C): " ,fruits)

idx = fruits.index("A")
print(idx)

item_to_remove = "Grapes"

if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")
else:
    print("insert a valid fruit...")