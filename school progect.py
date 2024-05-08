#Scool Project 
# Calculator Program:-
    
num1=float(input("Enter the first number :"))
a=input("This is our arithmatic opperators [+ ,- ,/ ,* ,% ,** ,//,pi,100% ] : ")
num2=float(input("Enter the second number :"))
import math 
if a=="+":
    print(num1+num2)
elif a=="-":
    print(num1-num2) 
elif a=="*":
    print(num1*num2)
elif a=="/":
    print(num1/num2)
elif a=="%":
    print(num1%num2)
elif a=="**":
    print(num1**num2)
elif a=="//":
    print(num1//num2)
elif a=="pi":
    print(num1*num2*math.pi) 
else :
    print("Opperator is not defiened so, we can't solve this problem.")

    












