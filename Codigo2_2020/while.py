num = 1
numm = 0
while num <= 5:
    print(num, "squared is: ",num**2)
    num = num + 1
else:
    print("Finished")

while numm < 5:
    numm = numm + 1
    if numm == 3:
        continue
    print(numm, "squared is: ", numm**2)