n= int(input("Enter number:"))
order = 0
a = n
while(a>0):
    order = order +1
    a=a//10
s = 0
num = n
while(num>0):
    d = num % 10
    print(d)
    s = s+(d ** order)
    print(s)
    num = num//10
if(s==n):
    print(n,"is a armstrong number.")
else:
    print(n,"is not a armstrong number")

