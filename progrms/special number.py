
n = int(input("Enter a number:"))
sum = 0
temp = n

while(temp):

    i= 1
    fact = 1
    r = temp% 10
    while(i<=r):
        fact = fact*i
        i=i+1
    sum = sum + fact
    temp= temp//10


if(sum == n):
    print(n,"is a special number.")
else:
    print(n,"is not a special number.")
