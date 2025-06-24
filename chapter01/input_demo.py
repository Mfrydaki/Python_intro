name =  input("Please enter your name: ")

print("Hello", name)

# year_of_birth = input("Please insert the year of birth: ")
# year_of_birth = int(year_of_birth)

year_of_birth = int(input("Please insert the year of birth: "))

print("You are", 2025 - year_of_birth, "years old")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height: "))

is_student = input("Are you student?(Yes/No): ").lower() == "yes" #(Yes, YES, yES, yes)

print(f"Hello {name}")

if is_student:
    print("You are student")
else:
    print("You are not a student")

print("Your age is {} and your height is {:.2f} meters".format(age,height))