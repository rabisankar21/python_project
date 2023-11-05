start_day = int(input("Enter the start day of the month(1-7):"))
num_of_days = int(input("Enter no. of days:"))
print("sun Mon Tues Wed Thrus Fri Sat")
print("---------------------------")
for i in range(start_day):
    print(end= " ")
    i = start_day -1
    for j in range(1,num_of_days + 1):
        if(i>6):
            print()
            i = 1
        else:
            i = i+1
        print(str(j) + " ", end= " ")