class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LINKED_nodes(): # this class head will point to the other nodes 
    def __init__(self):
        self.head=None
    
    def add(self,data):
        new_node=Node(data) # at this first node it hase next point to none and if this is the first node this is the head also 
        if self.head==None:
            self.head=new_node
            return
        current_node=self.head # take the the first head if the head is been set up
        while current_node.next: # go to the last node and then attched if next to the new node
            current_node=current_node.next
        current_node.next=new_node
    
    def display(self): # this is the function of the class linkled lilst so it can acces the object made through this class to other class
        current=self.head # head is the first node that we made here
        while current:
            print(f"{current.data}",end="->")
            current=current.next # move the node to next so we can acces the next node and its next pointing data 
        print("NONE")

ob1=LINKED_nodes() # THIS WILL MAKE THE OBJECT AND THEN WE CAN USE THE FUCNTOIN FOR THIS OBJECT THATA EXIST IN THIS LIBNKED LIST CLASS and the head for us 
ob1.add(10)
ob1.add(20)# --:> these nodes will made in the class Node throuGH lINKED_list
ob1.add(340)
ob1.display()