


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_end(head,n):
        if(head == None):
            head = Node(n)
            return head
        else:
            temp = head
            while(temp):
                prev = temp
                temp = temp.next
            newnode = Node(n)
            prev.next = newnode
            return head

def display(head):
        temp = head
        if(temp == None):
            print("Empty list")
        while(temp):
            print(temp.data)
            temp = temp.next

def insert_first(head,n):
        temp = head
        newnode = Node(n)
        newnode.next = temp
        head = newnode
        return head

def count(head):
        temp = head
        c = 0
        if(temp == None):
            print("Empty list")
            return c
        while(temp):
            c= c+1
            temp = temp.next
        return c
def search(head,n):
        temp = head
        pos = 0
        if(temp == None):
            print("Empty list")
            return 0
        while(temp):
            pos = pos+1
            if(temp.data == n):
                return pos
            temp = temp.next
        return -1

# def deletion(head,n):
#         temp = head
#         if(temp == None):
#             print("Empty list")
#             return head
#         elif(temp.data == n):
#             print("deleted item = ",temp.data)
#             head = temp.next
#             return head
#         else:
#             prev = temp
#             temp = prev.next
#             while(temp):
#                 if(temp.data == n):
#                     nitem = temp.next
#                     prev.next = nitem
#                     print("Delted item : ",temp.data)
#                     return head
#                 prev = temp
#                 temp = temp.next
#             print("Item not found")
#             return head




print("1.Insert End")
print("2. Display")
print("3. Insert first")
print("4. Count")
print("5. Search")
print("6. Deletion")
print("0. Exit")

head = None
while True:
    ch = int(input("Enter Your choice: "))
    if(ch == 1):
        n = int(input("Enter data: "))
        head = insert_end(head,n)
    elif(ch == 2):
        display(head)
    elif(ch == 3):
        n = int(input("Enter data: "))
        head = insert_first(head,n)
    elif(ch == 4):
        n = count(head)
        if(n>0):
            print("No of elements = ",n)
    elif(ch == 5):
        n = int(input("Enter data which you want : "))
        pos = search(head,n)
        if(pos>0):
            print("Item is in ",pos,"th position")
        else:
            print("item not found")
    elif(ch == 6):
        n = int(input("enter data which you want to delete : "))
        head = deletion(head,n)
    elif(ch == 0):
        break
    else:
        print("wrong Input")
        break

