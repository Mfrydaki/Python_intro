def main():
    students = {

      "Alice" : [85],
      "Bob" :[70],
      "Charlie" : [90],
      "Diana" : [95],
      "Elsa" : [50]
}
  
    #Find the student with the name lowest with alphabetic order
    student_with_min_grd = min(students) 
    print(student_with_min_grd)

    #Find student with min grade
    student_with_min_grd = min(students, key= students.get)
    print(student_with_min_grd)

    #Find student with the sortest name by lenght
    student_with_shortest_name = min(students, key=len)
    print(student_with_shortest_name)


if __name__ == "__main__":
    main()