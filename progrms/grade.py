print("Enter the marks of four subject:")
sub1 = int(input("1st subject:"))
sub2 = int(input("2nd subject:"))
sub3 = int(input("3rd subject:"))
sub4 = int(input("4th subject:"))
total = sub1 + sub2 + sub3 + sub4
print("Total marks = ", total)
agg = (total / 4)
print("Aggregate marks = ", agg)
per = (total/(4*100))*100
print(per)
if per>=60:
    print("1st Div")
elif per>= 45 and per< 60:
    print("2nd Div")
elif per>= 30 and per<45:
    print("3rd Div")
else:
    print("Fail")



