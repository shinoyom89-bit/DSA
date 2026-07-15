class queue():
    def __init__(self):
        self.stack=[]
        self.queue=[]

    def push(self,val):
        self.queue.append(val)
    
    def size(self):
        print(len(self.queue))

    def remove(self):
        if self.queue:
            length=len(self.queue)
            for i in range(1,length):
                self.stack.append(self.queue[i])

            print(self.queue[0])
            self.queue=self.stack
            self.stack=None
    def first(self):
        return self.queue[0]
    def display(self):
        print(self.queue)
q=queue()
q.push(8)
q.push(32)
q.push(45)
q.push(3)
q.push(2)
q.display()
first=q.first()
print(first)
print("this is the size of the queue :",end="")
q.size()
q.remove()
q.display()
