import os
import string

def word_freq(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    if ''in d:
        del d['']
    
    return d
    
def split_word(s):
    s=s.lower()
    s=s.replace("\n"," ")
    s=s.split(" ")
    s=[punct.strip(string.punctuation)for punct in s]
    return s

def mod(d):
    n=0
    for i in d:
        temp=d[i]*d[i]
        n=n+temp
    n=n**0.5
    return (n)

def vector(dict1,dict2):
    temp=0
    for i in dict1:
        for j in dict2:
            if i==j:
                temp+=dict1[i]*dict2[j]
    return temp

def plagiarism(path):
    l=[i for i in os.listdir(path) if i.endswith('.txt')]
    os.chdir(path)
    x1=[]
    for file1 in l:
        T1=open(file1,'r')
        f1=str(T1.read())
        f1=split_word(f1)
        x2=[]
        for file2 in l:
            T2=open(file2,'r')
            f2=str(T2.read())
            f2=split_word(f2)
            dict1=word_freq(f1)
            dict2=word_freq(f2)
            """calculations"""
            f1mod=mod(dict1)
            f2mod=mod(dict2)
            n=vector(dict1,dict2)
            plag_percent=(n)*100/((f1mod)*(f2mod))
            plag_percent=round(plag_percent,2)
            if(file1 == file2):
                plag_percent = None
            x2.append(plag_percent)
        x1.append(x2)
    return x1

path=input("enter the path:/n")
x=plagiarism(path)
l=[i for i in os.listdir(path) if i.endswith('.txt')]
os.chdir(path)
k=0
for i in x:
    print("file name:",l[k],"plagiarism check with all files",i)
    k=k+1



    
    
    
    
