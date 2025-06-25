import random

random_numbers = []

for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)
print (random_numbers)


#Finds the first even number
for num in random_numbers:
    if num % 2 == 0:
        even = num
        print(even)
        break

#Finds the last even number
for num in random_numbers:
    if num % 2 == 0:
     even = num
print (even)
