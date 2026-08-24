class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        self.currMinVal = 99999
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.currMinVal > val:
            self.currMinVal = val
        self.minStack.append(self.currMinVal)

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
            self.stack.pop()
            if self.minStack:
                self.currMinVal = self.minStack[-1]
            else:
                self.currMinVal = 999999
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
