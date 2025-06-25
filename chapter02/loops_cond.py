a = range (10)
print(f"Typr of a: {type(a)}")

for i in range(10):
 if i  == 5:
   break
 print(i , end=" ") 
print()

for i in range(10):
  if i == 5:
    continue
  print(i , end=" ") 
print()

for i in range(10):
  if i == 5:
    break
  print(i , end=" ") 
else:
  print("Loop ended normaly")

print()

#List of fruits
fruits = ["Banana", "Orange", "Mango","Grapes"]

fruits_to_check = "Banana"

for fruit in fruits:
  if fruit == fruits_to_check:
    print(f"{fruits_to_check} is in list")
    break
else:
  print(f"{fruits_to_check} not in list")

#Happy hour
print("Why do Python dev never get lost?")
print("Because they always know where "in" is!")

if fruits_to_check in fruits:
  print(f"{fruits_to_check} is in list")
else:
  print(f"{fruits_to_check} not in list")

print("One line exe")
print(f"{fruits_to_check} is {"in" if fruits_to_check in fruits else "not in"} the list")