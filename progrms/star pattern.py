row = int(input("Enter number of rows:"))
if(row <= 0):
    print("Wrong input.")
else:
    if(row % 2 == 0):
        print("please enter a odd number.")
    else:
        n = (row // 2) +1
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print(" ")
        for i in range(n - 2, -1, -1):
            for j in range(n - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print(" ")
