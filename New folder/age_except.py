class AgeException(Exception):
    pass
age= int(input("age"))
try:
     if not (age>=18 and age<=35):
         raise AgeException("not valid age")
     print("sucessfull")
   
