def department_id_generator(department):
    last_id = 0 

    def generate_id():
     nonlocal last_id
     last_idast_id += 1
     return f"{department}-{last_id}",last_id
    
    return generate_id
    
def main():
   python_id_gen = department_id_generator("Python")
   android_id_gen = department_id_generator("Android")

   print(python_id_gen()) #('Python -1', 1)
   print(python_id_gen())




if __name__ == "__main__":
   main()