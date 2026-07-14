class dynamic_Array(): 
    def __init__(self,capacity):
        self.size=0
        self.capacity=capacity
        self.arr=[None]*capacity # empty array of the provided capacity
    
    def get(self,n :int ) -> int:
        return self.arr[n]
    
    def insert(self,val,n):
        self.arr[n]=val

    def popback(self):
        self.size-=1
        return self.arr[self.size]
    
    def get_size(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def pushback(self,val):           #0 1 2 3  so to not get array out of bounce we use resize 
        if self.size==self.capacity: #[1 2 3]
            self.resize()
        self.arr[self.size]=val
        self.size+=1 # increment the size by one when element is added

    def resize(self):
        new_Ar=[None]*(self.capacity*2)
        for i in range(self.size):
            new_Ar[i]=self.arr[i]
        self.arr=new_Ar # new array of increased capacity
        self.capacity=2*self.capacity # update the capacity too if not updated then cause array out of bounce too when the new arr will full the self,size index will not be there thats why 
