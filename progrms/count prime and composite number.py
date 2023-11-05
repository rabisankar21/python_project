t_prime = 0
t_composite = 0
while(1):
    num = int(input("Enter no."))
    if(num == 1):
        break
    flag = 0
    for i in range(2,num):
        if(num % i == 0):
            flag = 1
            break
    if(flag == 1):
        t_composite += 1
    else:
        t_prime += 1
print("Total composite = ",t_composite)
print("Total prime: ",t_prime)