file1=input()
sum1=0
with open(file1) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            sum1=sum1+1
    print(sum1)
