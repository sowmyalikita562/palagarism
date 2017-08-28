from directory_list import*
from check_str import*
def LCS():
    for f1 in range(0,len(dir_list)):
        for f2 in range(0,len(dir_list)):
            if f1!=f2 and f1<f2:
                file_name=dir_list[f1]
                file1=open(file_name,"r")
                file_name2=dir_list[f2]
                file2=open(file_name2,"r")
                y=[]
                x=[]
                for line in file1:
                    p=line.split()
                    for i in range(0,len(p)):
                        p[i]=check_str(p[i])
                    y.extend(p)
                    p=[]
                for line2 in file2:
                    q=line2.split()
                    for i in range(0,len(q)):
                        q[i]=check_str(q[i])
                    x.extend(q)
                    q=[]
                #print(y)
                #print(x)
                out=[]
                max1=0
                sum1=0
                for i in range(0,len(y)):
                    l=i
                    for j in range(0,len(x)):
                        m=j
                    # print(y[i],x[j])
                        while y[i]==x[j]:
                 #           print("loop entered")
                            sum1=sum1+len(y[i])
                            max1=sum1
                  #          print("sum in loop",sum1,end=" ")
                            i+=1
                            j+=1
                            
                            if i>=len(y) or j>=len(x):
                                break
                        i=l
                        j=m
                        max1=sum1
                   #     print("sum1 out of loop",max1)
                        sum1=0
                        if len(out)==0:
                            t=0
                        else:
                            t=max(out)
                            
                    #    print("max in out",t)
                        if max1>t:
                            out.append(max1)
                    
                #print(out)
                
                mul=1
                try:
                    #for i in out:
                    lcs=int(max(out))
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
                    f.close()
                    with open(file_name2) as f:
                        while True:
                            c = f.read(1)
                            if not c:
                                break
                            else:
                                sum1=sum1+1
                    f.close()
                    print("the length of LCS is:",max(out))
                    k=(mul/sum1)*100
                    print(str(file_name)+"\t"+str(file_name2)+"\t"+str(k)+"%")
                except ValueError:
                    print("the length of LCS is: Empty")
                    print(str(file_name)+"\t"+str(file_name2)+"\t"+"0.0%")
                file1.close()
                file2.close()
                file1=open("output.txt","a+")
                file1.write(str(file_name)+"\t"+str(file_name2)+"\t"+str(k)+"%"+"\n")
                file1.close()
                
                


                   

