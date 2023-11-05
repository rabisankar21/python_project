n= int(input("Number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(1,2*i+2):
        if(j%2 == 0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()