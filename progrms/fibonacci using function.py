def Fibonacci(n):
    a, b = 0, 1
    if (n <= 0):
        print("Please enter a positive integer")
    elif (n == 1):
        print(a,end=" ")
    else:
        for i in range(1,n + 1):
            print(a,end=" ")
            c = a + b
            a = b
            b = c


# Driver Program
m = int(input("Enter how many terms?"))
Fibonacci(m)