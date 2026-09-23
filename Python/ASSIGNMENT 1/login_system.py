def setpassword(validate=False):
    while True:
        password = input("Enter Password : " if validate else "Set Password : ")
        if password.isalnum() and len(password) >= 8:
            break
        else:
            print(
                "Invalid password, password should have alphabet, numbers and minimum length (8)"
            )
    return password


def validatePassword(valid_password):
    attempt = 3
    while attempt > 0:
        password = setpassword(True)
        if password == valid_password:
            return True
        else:
            attempt -= 1
            print(f"Invalid Password : {attempt} left!")
    return False


username = ""
password = ""
while True:
    print("Choose a option :\n 1. Signup\n 2. Login")
    option = int(input("Enter a option : "))
    match option:
        case 1:
            username = input("Enter Username :")
            password = setpassword()
            print("Signup Successfull")
        case 2:
            if username != "" and validatePassword(password):
                print(f"{username} Login Success")
            else:
                print("Login First!")
        case _:
            break
