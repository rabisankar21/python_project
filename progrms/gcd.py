def GCD(x,y):
    rem = x%y
    if(rem==0):
        return y
    else:
        return GCD(y,rem)
n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("GCD of ",n,"and",m,"is",GCD(n,m))