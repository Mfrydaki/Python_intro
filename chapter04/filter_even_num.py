numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

#even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(type(even_numbers))

for num in even_numbers:
    print(num, end=" ")

print()

#list- reusable
even_num_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_num_list)
print(even_num_list)

def even_num_func(n):
    return n % 2 == 0

my_list = list(filter(even_num_list, numbers))
print(my_list)

