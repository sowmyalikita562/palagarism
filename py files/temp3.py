import os.path                          #to import files from directory
from collections import Counter         #to count number of words 
import math                             #to round off the integer
import string                           #to remove punctuations 

path=input("Enter the path of dir")
a=os.listdir(path)
os.chdir(path)

def file_split(s):
        s=s.lower()
        s=s.replace("\n"," ").replace("\xa0"," ")
        s=s.split(" ")
        s=[word.strip(string.punctuation)for word in s]             #removing punctuations
        print (s)
        return s

def frequency(s1):
        d1=Counter(s1)
        if "" in d1:
            del (d1[""])
        return d1
    
def eu_numerator(d1,d2):
        L=[]
        for i in d1:
            for j in d2:
                if i==j:
                    L.append(d1[i]*d2[j])
        return sum(L)

def eu_denominator(d):
        sum1=0
        for i in d:
            sum1+=(d[i])**2
        return (sum1**(1/2))
    
def plagiarism(f1,f2):

    s1=file_split(f1.read())
    s2=file_split(f2.read())
    d1=frequency(s1)
    d2=frequency(s2)
    numer=eu_numerator(d1,d2)
    denom=(eu_denominator(d1))*(eu_denominator(d2))
    return round((numer/denom)*100)


final=[]
for i in range (len(a)):
    for j in range (len(a)):
        if i==j:
            final.append("None")
        else:
            f1=open(a[i],"r")
            f2=open(a[j],"r")
            final.append(plagiarism(f1,f2))
            f1.close()
            f2.close()
    print(final,"\n")
    final=[]
