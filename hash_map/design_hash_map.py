class list_node():
    def __init__(self,key=-1,val=-1,next=None):
        self.next=next
        self.key=key
        self.val=val

class map():
    def __init__(self):
        self.map=[ list_node() for i in range(1000)] # here each element of this array will be node made by __init__
    
    def get_index(self,key):
        return self.key%1000
    
    def put(self,val,key):
        curr=self.map[self.get_index(key)] # check if the same key is existed or not
        while curr.next:
            if curr.next.key==key:
                curr.next.val=val
                return
            curr=curr.next
        curr.next=list_node(key=key,val=val) # point to  the next node on the the colloision] and handle the case when it is the first key val so dummy point to the first node if it is first 
    def get(self,key):
        curr=self.map[self.get_index(key)].next
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1
    
    def delete(self,key):
        curr=self.map[self.get_index(key)]
        while curr and curr.next:
            if curr.next.key==key:
                curr.next=curr.next.next
                return
        return -1