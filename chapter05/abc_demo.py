from abc import ABC , abstractmethod

class AbstractStudentDAO(ABC):
    """
    Defines the students DAO API
    """

    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError()
    
    @abstractmethod
    def getOne(self, student_id):
        raise NotImplementedError()


#Student Implementation
class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    
    def insert(self, student):
        student_id = student["id"]
        self.students[student_id] = student
        print(f"Inserted student with ID: {student_id}")
    

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found")
    
    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with id {student_id} ")
        else:
            print(f"Student with id {student_id} not found")

    def getOne(self, student_id):
        return self.students.get(student_id, None)
    
    #inventory system
class AbstractInventory(ABC):
       
        @abstractmethod
        def add_item(self, item):
            raise NotImplementedError()
        
        @abstractmethod
        def remove_item(self, item_name_to_remove):
           raise NotImplementedError()

    
class Inventory(AbstractInventory):
        def __init__(self):
            self.items = []
        
        def add_item(self, item):
            self.items.append(item)
        
        def remove_item(self, item_name_to_remove):
            for item in self.items:
                if item.name == item_name_to_remove:
                    self.items.remove(item)
                    print(f"Removed item: {item_name_to_remove}")
                    return
                print(f"Item not found: {item_name_to_remove}")

class Item:
        def __init__(self, name):
            self.name = name
    
        def __str__(self):
            return self.name
        
#Main function
def main():
    student_d= StudentImpl()
    student_d.insert({'id':1, 'name':"Marika"})
    student_d.insert({'id':2, 'name': "Tina"})

    student_d.update(1, {'id':1, 'name':"Maria"})
        
    st = student_d.getOne(1)
    print(st) #{'id':1, 'name':'Maria'}
    student_d.delete(2)
    
    # Inventory testing
    inventory = Inventory()
    item1 = Item("Notebook")
    item2 = Item("Pen")

    inventory.add_item(item1)
    inventory.add_item(item2)

    inventory.remove_item("Pen")
    inventory.remove_item("Eraser")

if __name__ == "__main__":
        main()