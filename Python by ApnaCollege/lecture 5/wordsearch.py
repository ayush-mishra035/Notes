with open("sample2.txt","r") as f:
    data = f.readline()
    while data:
        data = f.readline()
        print(data)

    