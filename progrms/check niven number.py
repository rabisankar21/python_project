 # A niven number which is divisible by the sum of digits. Ex - 111 = 1+1+1 = 3, 111 is divisible by 3
def checkniven(n):
     sum = 0
     temp = n
     while temp > 0:
         sum = sum + temp % 10
         temp = temp // 10
     return n % sum == 0

n = int(input("Enter Number: "))

if(checkniven(n)):
     print("Yes")
else:
     print("No")

