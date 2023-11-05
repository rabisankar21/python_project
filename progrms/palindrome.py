n = int(input("Enter Number:"))
temp = n
rev = 0
while(temp>0):
    dig = temp%10
    rev = rev*10 + dig
    temp=temp//10
if(n==rev):
    print(n,"is a palindrome number.")
else:
    print(n,"is not a palindrome number")