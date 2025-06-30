def decrypt_message(message : str):
    decrypted_message= ""

    for char in message:
        if not char.isnumeric():
            decrypted_message += char
    return decrypted_message



def main():
    #432H345456GHo 2234545"
    strange_message = "432H345e456Llo 223!4545"

    decrypted_message = decrypt_message(strange_message)
    print(decrypted_message)


if __name__ == "__main__":
    main()