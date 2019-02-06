f=open(r"C:\Users\harpreet\OneDrive\Documents\exe.txt","w")
f.write("I am the best") #write content if file alread exit all cintent are erase
f.close()
f=open(r"C:\Users\harpreet\OneDrive\Documents\exe.txt","r")
print(f.read())
