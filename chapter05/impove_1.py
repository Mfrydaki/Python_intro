def upscale_grades(grades):
    upscaled = [grade +1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_passed(grades):
    passed = [grade for grade in grades if grade >= 5]
    return passed


def categorize_grades(grades):
    passed = [grade for grade in grades if grade >= 5 and grade < 10 ]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return failed, passed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    grades = [ 7, 5, 9, 10 , 3, 7, 8]

    upscaled_grades = upscale_grades(grades)
    print (f"Initial grades: {grades}")
    print (f"Upscaled grades: {upscaled_grades}")

    passed_gd , failed_gd , honored_gd = categorize_grades(grades=grades)

    print (f"Passed students: {passed_gd}")
    print (f"Failed students: {failed_gd}")
    print (f"Honored students: {honored_gd}")






if __name__ == "__main__":
    main()