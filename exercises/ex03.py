"""
Construct an iterator which iterates through the squares of the numbers 10 - 20 in three ways: using an iterator (class), using a generator (function), and using a generator expression (comprehension).

"""
#Iterator
class Iterator:
    def __iter__(self):
        self.n = 9 # starts from 10
        return self
    
    def __next__(self):
     self.n += 1
     if self.n <= 20 :
            return self.n ** 2
     else:
            raise StopIteration
            
for n in Iterator():
    print(n)



#Generator
def MyIterator():
    for i in range(10, 21):
        yield i 

for i in MyIterator():
    print(i*i)
 


#Generator comprehension
g = (i**i for i in range (10,21))

for i in g:
    print(i)




    
