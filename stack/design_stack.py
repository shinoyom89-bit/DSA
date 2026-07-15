class stack():
    def __init__(self):
        self.stack=[]

    def pop(self):
        if self.is_empty:
            raise IndexError("stack is empty ")
        self.stack.pop()
    
    def is_empty(self):
        return self.stack.len==0

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")        
        return self.stack[-1]
    def add(self,n):
        self.stack.append[n]
    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.stack[-1]