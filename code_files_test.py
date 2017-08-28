from directory_list import*
from synonyms import*
def code_files_test(keywords,ext):
    for f1 in range(0,len(dir_list)):
        for f2 in range(0,len(dir_list)):
            
            if f1!=f2 and f1<f2:
                filename = dir_list[f1]
                filename2=dir_list[f2]
                if filename.split(".")[-1]==filename2.split(".")[-1]==ext:
                    file = open(filename, "r")
                    d={}
                    for line in file:
                        s=[]
                        count=0
                        s=line.split()
                        
                        for i in s:
                            if i not in d.keys():
                                
                                d[i]=int("1")
                            elif i in d.keys():
                                count=d.get(i)
                                count=count+1
                                d[i]=count
                                
                       
                    #print(d)
                    file = open(filename2, "r")
                    d2={}
                    for line in file:
                        s=[]
                        count=0
                        s=line.split()
                        #print(s)
                        for i in s:
                            if i not in d2.keys():
                                d2[i]=int("1")
                            elif i in d2.keys():
                                count=d2.get(i)
                                count=count+1
                                d2[i]=count
                    #print(d2)
                    count=0
                    count2=0
                    for i in d.keys():
                        if i in keywords:
                            count2=count2+1
                            if i in d2.keys():
                                if d.get(i)==d2.get(i):
                                    count=count+1
                                    #print(count)
                           
                                
                    per=count/count2
                    per=int(per*100)
                    print(filename+"\t"+filename2+"\t"+str(per)+"%"+"\n")
                    the_file=open("output.txt", "a+")
                   
                    the_file.write(filename+"\t"+filename2+"\t"+str(per)+"%"+"\n")
                    the_file.close()
        #the_file.write("\n\n\n")
        
                                

