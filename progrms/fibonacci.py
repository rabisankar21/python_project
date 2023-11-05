n= int(input("Enter how many terms"))
a,b = 0,1
if(n<=0):
    print("Please enter a positive integer")
elif(n==1):
    print(a)
else:
    for i in range(1,n+1):
        print(a)
        c= a+b
        a=b
        b=c