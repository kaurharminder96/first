try:
    a=int(input("Enter the value of A"))
    b=int(input("enter the value of B"))
    print(a+b)
    print(a/b)
except ArithmeticError:
    print("No. is divisible by 0");
    
