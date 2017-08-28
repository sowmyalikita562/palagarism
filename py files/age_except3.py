class ageException(Exception):
    pass
age1= int(input("age1"))
try:
     if not (age1>=18 and age1<=35):
         raise ageException("not valid age")
     print("sucessfull")
   
