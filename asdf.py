#job no-8
a=int(input("This is the first angle :"))
b=int(input("This is the second angle :"))
c=int(input("This is the third angle :"))
 
if a == 0 or b ==0 or c== 0 :
    print("No, we can't make a triangle.")
elif a+b+c == 180 :
    print("Yes, we can make a triangle.")
    
else :
     print("No, we can't make a triangle.")

