square = []

for i in range(6):
    square.append(i*i)

print(square)

sq=[i*i for i in range(6)]
print(sq)


# another example

nums = [ -2, -1, 0, 1, 2]

nums =[ 0 if val <0 else val for val in nums]
print(nums)