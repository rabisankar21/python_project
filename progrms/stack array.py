from array import *
MAX = 5
class stack_array:
    stack = array('i',[0,0,0,0,0])
    top = -1
    def push(self,n):
        if(self.top == MAX-1):
            print("Stack overflow")
        else:
            self.top= self.top +1
            self.stack[self.top]= n
            print("One item added")

    def pop(self):
        if(self.top == -1):
            print("Empty stack")
        else:
            n = self.stack[self.top]
            self.top = self.top -1
            print("Deleted item = ",n)

    def display(self):
        if (self.top == -1):
            print("Empty stack")
        else:
            i = self.top
            while(i>=0):
                print(self.stack[i])
                i= i-1

print("1.push")
print("2.pop")
print("3.display")
print("4.exit")

s= stack_array()

while True:
    ch = int(input("Enter your choice: "))
    if(ch==1):
        n = int(input("Enter data : "))
        s.push(n)
    elif(ch==2):
        s.pop()
    elif(ch==3):
        s.display()
    elif(ch==0):
        break
    else:
        print("Wrong input")
        break
