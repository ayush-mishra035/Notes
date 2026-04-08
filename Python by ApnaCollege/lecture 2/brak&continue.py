i = 1

while (i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1

print("outside loop now ....")


# skip multiple of 3

i = 1       
while(i<=10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1

# odd number
i = 1

while(i<=10):
    if(i%2==0):
        i += 1
        continue
    print(i)
    i += 1