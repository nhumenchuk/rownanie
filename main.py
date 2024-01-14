import math
print('podaj a,b,c')
a=int(input("podaj a "))
b=int(input("podaj b "))
c=int(input("podaj c "))
delta=b**2-4*a*c
x1=(-b-math.sqrt(delta))/(2*a)
print('pierwsze rozwiązanie równania ',x1)
x2=(-b+math.sqrt(delta))/(2*a)
print('drugie rozwiązanie równania ',x2)