import random
a=random.randint(1,10)
i=0
while(i<3):
 b=int(input("Enter a number"))
 if(a==b):
   print("You Won")
   break
 elif(a>b):
   print("Try again Your no. small")
   i+=1
 elif(a<b):
   print("Try again your no. grater")
   i+=1
 else:
   print("you loss")
 

