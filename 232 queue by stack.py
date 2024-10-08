class MyQueue:
    def __init__(self): self.stack=[]        
    def push(self, x: int) -> None: self.stack.append(x)
    def pop(self) -> int:
        if len(self.stack)<1: return -1
        b=[]
        while self.stack:
            b.append(self.stack.pop())
        temp = b.pop()
        self.stack=[]
        while b:
            self.stack.append(b.pop())
        return temp

    def peek(self) -> int:
        b=[]
        while self.stack:
            b.append(self.stack.pop())
        temp = b.pop()
        self.stack=[temp]
        while b:
            self.stack.append(b.pop())
        return temp

    def empty(self) -> bool: return not self.stack 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
