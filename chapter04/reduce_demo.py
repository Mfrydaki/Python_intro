from functools import reduce

#list of numbers
my_ints = [1, 2, 3, 4, 5]

# x = 1+2= 3 , 3+3, 6+4, 10+5
result = reduce(lambda x , y : x + y, my_ints)
print(result)

result2 = reduce(lambda x, y : x * y , my_ints)
print(result2)
