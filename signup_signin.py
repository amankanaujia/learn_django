print("1. sign_up \n2. sign_in")
option = int(input("enter the option : "))
if option == 1:
    username = input("Enter the username : ")
    password = input("enter the password : ")
    print("sign up successfully.")
    username1 = input("Enter the username : ")
    password1 = input("enter the password : ")
    if username == username1 and password == password1:
        print("sign in successfully.")
if option == 2:
    print("please sign up first.")

