def input_float():
    while True:
        num = input("Please insert an float: ").strip() 

        if "." in num:
            parts = num.split(".")
            if len(parts) > 2:
                print("Only one dot at most please.")
            elif parts[0].isdigit() and parts[1].isdigit():
                return float(num)
            else:
                print("Only digits please.")

        else:
            if num.isdigit():
                return float(num)
            else:
                print("Only digits please.")

print(input_float())