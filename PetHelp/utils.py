def get_password_email():
    with open("C:\\Users\\Danail Lesev\\project\\PetHelp\\password.txt", "r") as f:
        psw = f.read()

    return psw
