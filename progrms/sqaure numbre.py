n = int(input("Enter the number:"))
i=1
while(i*i<n):
    i=i+1
if(i*i == n):
    print(n,"is a square number.")
else:
    print(n,"is not a square number.")