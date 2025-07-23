class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__ (self):
        return len(self.data)
    
    def __repr__(self):
        return f"DataCollection({self.data})"
    
def main():
        collection = DataCollection([1, 2, 3, 4, 5])

        print(f"DataCollection: {DataCollection}") 

        #iterate
        for item in collection:
            print(item)

        #unpacking
        a, b, c, d = collection
        print(a,c)

        #indexing
        print(f"Element at index 0: {collection[0]} ")

        #slicing
        print(collection[1:4])

        print(f"Lenght of collection: {len(collection)}")
        

if __name__ == "__main__":
     main()