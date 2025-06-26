def say_hello(name: str = "Coding Factory"):
    """
    print a greeting message.
    args:
     name (str) : The name to greet. Default value "Coding Factory"
    """
    print(f"Hello {name}")

def main():
    # say_hello(20)
    say_hello()
    say_hello("Marika")

    # print the documentation
    # say_hello(say_hello.__doc__)
    help(say_hello)
    pass

if __name__ == "__main__":
    main()