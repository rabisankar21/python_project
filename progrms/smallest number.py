a = int(input("Enter 1 st number:"))
b = int(input("Enter 2 nd number:"))
c = int(input("Enter 3rd number:"))
min = 0
if a<b and a<c:
    min = a
elif b<c:
    min = b
else:
    min = c
print(min , "is the minimum number")
