from functools import reduce

#list of numbers
my_ints = [1, 2, 3, 4, 5]

# x +y = 1+2= 3 -> x= 3, y = 2 ,3+2 = 5 -> x= 5 , y= 3 ...
result = reduce(lambda x , y : x + y, my_ints)
print(result)

result2 = reduce(lambda x, y : x * y , my_ints)
print(result2)
