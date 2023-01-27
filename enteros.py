import math

a = int(input("num escribir mucho: "))
b = int(input("num escribir mucho: "))
c = int(input("num escribir mucho: "))
disc = int(((b**2)-(4*a*c)))
 
if disc < 0:
    print("Ta mal no sale")
  

if disc == 0:
    print("tiene 1 soluçao")
if disc > 0:
    print("tiene 2 soluçao")
    
print((-b+math.sqrt(b**2-(4*a*c))/(2*a)))
print((-b-math.sqrt(b**2-(4*a*c))/(2*a)))
