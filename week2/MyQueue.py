class MyQueue:
    stack =[]
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        if len(self.stack1)==0:
            self.stack1.append(x)
        else:
            for i in self.stack1[::-1]:
                self.stack2.append(i)
            self.stack1.clear()
            self.stack1.append(x)
            for i in self.stack2[::-1]:
                self.stack1.append(i)
            self.stack2.clear()
    def pop(self) -> int:
        if len(self.stack1) != 0:
            item = self.stack1[-1]
            self.stack1.pop()  
            return item
        
    def peek(self) -> int:
        if len(self.stack1) != 0:
            return self.stack1[-1]
           
    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()