username = input("enter username :")
password = input("enter password :")

if(username == "admin" and password == "pass"):
    print("login sucessful!")
elif (username != "admin"):
     print("invalid username")
else:
     print("wrong password")