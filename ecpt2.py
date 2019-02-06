try:
    a=int(input("Enter the no."))
    b=int(input("Enter the no."))
    print(a/b)
except Exception as e:
    print(e)
print("###########################################")
try:
    a=int(input("Enter the no."))
    b=int(input("Enter the no."))
    raise ArithmeticError("Hello")
except Exception as e:
    print(e)
