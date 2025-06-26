class Student :
   pass

"""
A class that represents a student with a first name and a last name.

Attrs:
firstname(str): first name of the student.
lastname(str): last name of the student.
"""

def __init__(self, firstname: str, lastname: str):
   
   self.firstanme = firstname
   self.lastname = lastname

def main():
   st = Student("Bob", "M")
   print(f"First name is : {st.firstname}")
   print(f"Last name is : {st.lastname}")


if __name__ == "__main__":
  main()
