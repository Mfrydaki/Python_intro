
class Base:
    def __init__(self):
        self.pub = "I am public"

    def __private_method(self):
        return "This is a private"
    
    def get_private(self):
        return self.__private_method()
    
class Derived(Base):
     def __init__(self):
            super().__init__()
            self._pri = "I am new private var"
      
     def get_new_private_var(self):
            return self._pri
        
def main():
        
        base = Base()
        print(base.pub)
        print(base.get_private())

        derived = Derived()
        print(derived.pub)
        print(base.get_private())
        print(derived.get_new_private_var())
    
        pass


if __name__ == "__main__":
        main()