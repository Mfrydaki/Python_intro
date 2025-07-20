students = {

        "Alice" : [85, 92, 100],
        "Bob" :[70, 68, 99],
        "Charlie" : [90, 95, 94],
        "Diana" : [95, 98, 100],
        "Elsa" : []
}

def main():
    while True:
        try:
            threshold = int(input("Please insert a threshold (int): "))
        except ValueError:
            print("Invalid input.")
            continue

        average_grades = {
            student : round(sum(grades)/ len(grades), 2) # Calculate the average grade for the student and round it to 2 decimal places
            for student, grades in students.items()
            if grades and (sum(grades)/len(grades)) > threshold
            # Check if the student has any grades and if their average grade is greater than the threshold

            

            }

        for student, avg_grade in average_grades.items():
            print(f"{student}:{avg_grade}")
        break

if __name__== "__main__":
    main()