def exponential(n, x):
    # initialize sum of series
    sum = 1.0
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    return sum
    #print("e^x =", sum)

# Driver program to test above function
a = int(input("enter the value of n:"))
b = float(input("enter the value of x:"))
print("e^x = ",exponential(a, b))
#exponential(n, x)