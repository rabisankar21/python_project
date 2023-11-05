n = int(input())
inp = list(map(int, input().split(" ")))
a = int(input())
cd = []
flag = 0
for i in range(1 , len(inp)):
    if(inp[i-1]<=inp[i]):
        min1=inp[i-1]
    else:
        min1 = inp[i]
    if(min1 == a):
        ab = [i , i+1]
        flag = 1
    if(flag == 1):
        cd = cd + [ab]
        flag = 0

print(cd)



