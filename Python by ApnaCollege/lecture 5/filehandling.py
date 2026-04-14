f = open("sample.txt", "r") # file object
print(f.read())

data = f.readlines()
print(data)

data = f.readline()
print(data)

f.close()


# 
f = open("sample.txt","w")

f.write("Text to overwrite \n the complete data.")

f.close()