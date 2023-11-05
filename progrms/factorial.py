n=int(input("Enter the number:"))
fact = 1
if(n<0):
    print("Wrong input")
elif(n == 0):
    print("The factrorial of",n,"is",fact)
else:
    for i in range (1,n+1):
        fact = fact*i

    print("The factorial of", n, "is",fact)
