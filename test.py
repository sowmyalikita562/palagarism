file_name=input()
file1=open(file_name,"r")
file_name2=input()
file2=open(file_name2,"r")
y=[]
x=[]
for line in file1:
    p=line.split()
    y.extend(p)
    p=[]
for line2 in file2:
    q=line2.split()
    x.extend(q)
    q=[]
print(y)
print(x)
out=[]
max1=0
sum1=0
for i in range(0,len(y)):
    l=i
    for j in range(0,len(x)):
        m=j
        print(y[i],x[j])
        while y[i]==x[j]:
            print("loop entered")
            sum1=sum1+len(y[i])
            max1=sum1
            print("sum in loop",sum1,end=" ")
            i+=1
            j+=1
            
            if i>=len(y) or j>=len(x):
                break
        i=l
        j=m
        max1=sum1
        print("sum1 out of loop",max1)
        sum1=0
        if len(out)==0:
            t=0
        else:
            t=max(out)
            
        print("max in out",t)
        if max1>t:
            out.append(max1)
    
print(out)
lcs=int(max(out))
mul=1
try:
    #for i in out:
    mul=lcs*2
    file1.close()
    file2.close()
    sum1=0
    with open(file_name) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                sum1=sum1+1
    with open(file_name2) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                sum1=sum1+1
    print("the length of LCS is:",max(out))
    print("mathing between and =",(mul/sum1)*100,"%")
except ValueError:
    print("the length of LCS is: Empty")
    print("mathing between and =0.00%")
file1.close()
file2.close()
f.close()


