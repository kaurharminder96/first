class A:
 def a1(self):
     print("Hello")
class B(A):
 def b1(self):
     print("I am harminder")
 def a1(self):
     print("Hi")
class C(B):
 def c1(self):
     print("byee")
c=C()
c.a1()
c.b1()
c.c1()
print("//////////////////////////////////")
class A:
 def a1(self):
     print("Hello")
class B:
 def b1(self):
     print("I am harminder")
class C(A,B):
 def c1(self):
     print("HW r uh")
class D(C):
 def d1(self):
     print("Bye")
d=D()
d.a1()
d.b1()
d.c1()
d.d1()
