#define a tuple of students
students = "Alice", "Bob", "Charlie"
print(f"{students}: {type(students)}")

print()

#iteration
for index, student in enumerate(students):
    print(f"{index}:{student}")

print()

for student in students:
    print(student)

print()

first_st, second_st, third_st = students
# students[0], students[1], students[2]
print(f"first_st: {first_st}")
print(f"second_st: {second_st}")
print(f"third_st: {third_st}")

print()

#Update 
students = list(students)
students[0] = "Helen"
students = tuple(students)

print(f"{students}, {type(students)}")