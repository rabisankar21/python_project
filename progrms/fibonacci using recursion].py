def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


m = int(input("Enter how many terms? "))  # take input from the user

if m <= 0:  # check if the number is valid
    print("Please enter a positive integer")
else:
    for i in range(m):
        print(Fibonacci(i),end=" ")