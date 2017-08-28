from directory_list import*
from check_str import*
def finger_print(n):
    for f1 in range(0,len(dir_list)):
        for f2 in range(0,len(dir_list)):
            if f1!=f2 and f1<f2:
                file_name=dir_list[f1]
                file1=open(file_name,"r")
                file_name2=dir_list[f2]
                file2=open(file_name2,"r")
                y=[]
                x=[]
                s1=""
                s2=""
                out=[]
                out1=[]
                for line in file1:
                    p=line.split()
                    for i in range(0,len(p)):
                        p[i]=check_str(p[i])
                    y.extend(p)
                    p=[]
                for i in y:
                    if len(i)>3:
                        s1=s1+i   
                for line2 in file2:
                    q=line2.split()
                    for i in range(0,len(q)):
                        q[i]=check_str(q[i])
                    x.extend(q)
                    q=[]
                for i in x:
                    if len(i)>3:
                        s2=s2+i
               
                end1=s1[(len(s1))-n:len(s1)]
                #print(end1)
                end2=s2[(len(s2))-n:len(s2)]
                
                token_s1=[]
                token_s2=[]
                i=0
                j=i+n
                dict_s1={}
                dict_s2={}
                for i in range(0,len(s1)):
                    j=i+n
                    k=s1[i:j]
                    token_s1.append(k)
                    if i==len(s1)-n:
                        break
               
                for i in token_s1:
                    sum1=0
                    k=n-1
                    for j in i:
                        sum1=sum1+(ord(j)*(n**(k)))
                        k=k-1
                    sum1=sum1%10007
                    dict_s1[i]=sum1
                #print(dict_s1)
                i=0
                j=n
                for i in range(0,len(s2)):
                    j=i+n
                    k=s2[i:j]
                    token_s2.append(k)
                    if i==len(s2)-n:
                        break
               
                i=0
                j=0
                for i in token_s2:
                    sum1=0
                    k=n-1
                    for j in i:
                        sum1=sum1+(ord(j)*(n**(k)))
                        k=k-1
                    sum1=sum1%10007
                    dict_s2[i]=sum1
                
                count=0
                for i in dict_s1.values():
                    for j in dict_s2.values():
                        if i==j:
                            count=count+1
                #print("similar",count)
                fprint=2*count/(len(dict_s1)+len(dict_s2))
                fprint=fprint*100
                print(file_name,"and",file_name2,"have",fprint,"% matching")
                file1=open("output.txt","a+")
                file1.write(str(file_name)+"\t"+str(file_name2)+"\t"+str(fprint)+"%"+"\n")
                file1.close()
                
                            
                
