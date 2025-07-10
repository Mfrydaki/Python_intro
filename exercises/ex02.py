"""
Construct an iterator that calculates the first 100 odd numbers and their sum.

"""

class OddNumbersIterator:
    def __iter__(self):
        self.n = -1
        return self
    
    def __next__(self):
        self.n += 2
        if self.n <=100:
            return self.n
        else:
            raise StopIteration
        
def main():
    print(sum(OddNumbersIterator()))

if __name__ == "__main__":
    main()

