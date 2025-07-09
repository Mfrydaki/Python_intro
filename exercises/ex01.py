"""Develop a script that implements a queue as FIFO"""

class Queue:
    def __init__(self):
        self.items = []

    def queue_is_empty(self):
        return len(self.items) == 0 # if empty = True
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.queue_is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"
    
    def peek(self):
        if not self.queue_is_empty():
            return self.items[0]  #returns first item without deleting it
        else:
            return "Queue is empty!"
    
    def display(self):
        print("Current queue:", self.items)
    

def main():
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("C")
    queue.enqueue("A")

    queue.display()
    print("Peek:", queue.peek())       #shows first item without removing it
    print("Dequeued:", queue.dequeue())  
    print("Peek after dequeue:", queue.peek()) 
    queue.display()


if __name__ == "__main__":
    main()
