import string
import random

#sting to list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def generate_password():
    """
    Generate a random password based on the user specified lenght.
    """
    try:
        password_lenth = int(input("Insert the password lenght: "))

        if password_lenth <= 0:
            print("Password lenght must be a positive number.")

    except ValueError:
        print("Invalid input. Please provide a positive integer.")
        return
    
    random.shuffle(characters)

    password = []

    for i in range(password_lenth):
       password.append(random.choice(characters))

    random.shuffle(password)

    #list to string
    password = "".join(password)

    print(f"Generated password: {password}")


def main():
    while True:
        option = input("\nDo you want to create a password? ('y' or 'q' for quit.): ")

        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong input.")


if __name__ == "__main__":
    main()