from array import *
MAX = 5
class circular_Queue:
    cqueue = array('i',[0,0,0,0,0])
    rear = 0
    front = 0
    def insertion(self,n):
        if((self.rear+1)%MAX == self.front):
            print("Queue overflow")
        else:
            self.cqueue[self.rear]=n
            self.rear= (self.rear+1)%MAX
            print("One item added")
    def deletion(self):
        if(self.rear == self.front):
            print("Empty Queue")
        else:
            n= self.cqueue[self.front]
            self.front = (self.front+1)%MAX
            print("deleted item = ",n)
    def display(self):
        if(self.rear==self.front):
            print("Empty Queue")
        else:
            i=self.front
            while(i!=self.rear):
                print(self.cqueue[i])
                i=(i+1)%MAX

cq = circular_Queue()
print("1.insertion")
print("2.deletion")
print("3.display")
print("4.exit")
while True:
    ch = int(input("Enter Your choise: "))
    if(ch == 1):
        n = int(input("Enter data : "))
        cq.insertion(n)
    elif(ch == 2):

        cq.deletion()
    elif(ch == 3):
        cq.display()
    elif(ch == 0):
        break
    else:
        print("Wrong input")
        break