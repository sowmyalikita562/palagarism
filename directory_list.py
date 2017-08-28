import os
print("url of the directory please!!")
n=input()
n=n.replace("/","\\")
path=n
os.chdir(n)
dir_list=os.listdir(n)
print(dir_list)
print(path)
