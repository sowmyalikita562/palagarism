from directory_list import*
from synonyms import*
from finger_print import finger_print
from code_files_test import*
import math
from combined_bag import Bag_of_words
from LCS import LCS
class project:
    def Bag_of_words(self):
        Bag_of_words()
    def LCS(self):
        LCS()
    def code_files_test(self,arr,ext):
        code_files_test(arr,ext)
    def finger_print(self,n):
        finger_print(n)
print("choose the method to check plagarism:")
print("\n","1.bag of wors","\n","2.LCS","\n","3.python files","\n","4.C files","\n","5.Finger printing")
n=int(input())
k=project()
if n==1:
    print("output of bag of words")
    k.Bag_of_words()
elif n==2:
    print("output of lcs")
    k.LCS()
elif n==3:
    print("output of python files plagarism")
    ext="py"
    k.code_files_test(python,ext)
elif n==4:
    print("output of C files plagarism")
    ext="c"
    k.code_files_test(c,ext)
elif n==5:
    print("output of finger printing technique")
    print("enter n value")
    n=int(input())
    k.finger_print(n)
