username = input("enter username:")
password = input("enter password:")

if(username == "admin" and password == "pass"):
    print("login successful!")
else:
    if(username != "admin"):
        print("invalid username")
    else:
        print("wrong password")