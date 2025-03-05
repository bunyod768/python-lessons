
ask = int(input("Enter a number: "))
i =2

while i < ask:
    j=1
    count =0
    while j <= i:
        if i % j == 0:
            count += 1
        j+=1
    if count ==2:
        print(i)
    i+=1
    count =0



