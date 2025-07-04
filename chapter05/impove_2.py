

def upscaled_grades(student_grades):
    return{name: (grade +1 if grade <=9 else grade)for name, grade in student_grades.items()}

def filter_passed(student_grades):
    return {name :grade for name , grade in student_grades.items()if grade >= 5}

def categorize_grades(student_grades):
    passed ={name :grade for name, grade in student_grades.items() if 5 <= grade < 10 } #if grade >= 5 and grade <10
    failed = { name : grade for name, grade in student_grades.items() if grade <5}
    honors = { name : grade for name, grade in student_grades.items() if grade ==10}
    return failed, passed, honors

def calculate_average(student_grades):
    if student_grades:
        return sum(student_grades.values())/len(student_grades)
    return 0


def main():
    students_grades = {
        "Alice": 7,
        "Bob": 5,
        "Charlie": 9,
        "David": 10,
        "Eve": 3,
        "Frank": 6,
        "Grace": 8,
        "Heidi": 4,
        "Ivan": 10,
        "Judy": 2
 }
    print(f"Original grades: {students_grades}")

    up_grades= upscaled_grades(students_grades)
    print("Upscaled grades")


if __name__ == "__main__":
    main()