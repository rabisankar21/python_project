from array import *
MAX = 5
class queue_array:
    queue = array('i',[0,0,0,0,0])
    rear= -1
    front = -1
    def insertion(self,n):
        if(self.rear==MAX-1):
            print("Queue overflow")
        else:
            self.rear= self.rear+1
            self.queue[self.rear]= n
            print("One item added")
            # print(self.rear)

    def deletion(self):
        if(self.rear==self.front):
            print("Empty queue")
        else:
            self.front= self.front+1
            n=self.queue[self.front]
            print("Deleted item = ",n)
            # print(self.front)

    def display(self):
        if (self.rear == self.front):
            print("Empty queue")
        else:
            i = self.front+1
            while(i<=self.rear):
                print(self.queue[i])
                i = i+1

print("1.insertion")
print("2.deletion")
print("3.display")
print("4.exit")

q = queue_array()
while True:
    ch = int(input("Enter Your choise: "))
    if(ch == 1):
        n = int(input("Enter data : "))
        q.insertion(n)
    elif(ch == 2):

        q.deletion()
    elif(ch == 3):
        q.display()
    elif(ch == 0):
        break
    else:
        print("Wrong input")
        break
