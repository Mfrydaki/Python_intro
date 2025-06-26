choice = 'q'

if choice == "q" or choice == "Q":
    print("Quit")
else:
    print("Continue")

#OR

if choice.upper() == "Q":
    print("Quit")
else:
    print("Continue")

#OR

if choice in( "q", "Q"):
    print("Quit")
else:
    print("Continue")
     