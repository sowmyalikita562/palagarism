from directory_list import*
from check_str import*
import math
from string import punctuation
def Bag_of_words():
    matrix=[]
    
    for f1 in range(0,len(dir_list)):
        for f2 in range(0,len(dir_list)):
            l=[]
            if f1!=f2 and f1<f2:
                text1=dir_list[f1]
                text2=dir_list[f2]
                file1 = open(text1,"r")
                file_out=open("output.txt","a+")
                d={}
                for line in file1:
                    s=[]
                    count=0
                    s=line.split()
                    
                    for i in s:
                        i=check_str(i)
                        if i not in d.keys():
                            d[i]=int("1")
                        elif i in d.keys():
                            count=d.get(i)
                            count=count+1
                            d[i]=count
               # print(d)
                d2={}
                file2 = open(text2,"r")
                for line in file2:
                    s=[]
                    count=0
                    s=line.split()
                    for i in s:
                        i=check_str(i)
                        if i not in d2.keys():
                            d2[i]=int("1")
                        elif i in d2.keys():
                            count=d2.get(i)
                            count=count+1
                            d2[i]=count
                #print(d2)
                if "" in d:
                    del(d[""])
    
                if "" in d2:
                     del(d2[""])
   
                sum1=0
                for i in d.keys():
                    for  j in d2.keys():
                        if i==j:
                            sum1=sum1+(d.get(i)*d2.get(j))
                 #           print("i",i,"j","sum",sum1)
                #print("Dot product",sum1)
                sum2=0
                for i in d.values():
                    sum2=sum2+i**2
               # print("sum2",sum2)
                sum3=0
                for i in d2.values():
                    sum3=sum3+i**2
                #print("sum3",sum3)
                sum2=math.sqrt(sum2)
                sum3=math.sqrt(sum3)
                cosine=(sum1)/(sum2*sum3)
               

                file1.close()
                file2.close()
                print(str(text1)+"\t"+str(text2)+"\t"+str(cosine*100))
                
                file_out.write(str(text1)+"\t"+str(text2)+"\t"+str(cosine*100)+"\n")
 #file_out.write("***************************************************************")
                 file_out.close()
               
                

    
