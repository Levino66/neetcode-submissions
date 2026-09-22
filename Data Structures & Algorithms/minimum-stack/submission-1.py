class MinStack:

    def __init__(self):
        self.stack = []
        self.minorder = []

    def push(self, val: int) -> None:
        if (not self.stack) or val < self.stack[self.minorder[-1]]:
            self.minorder.append(len(self.stack))
            
        self.stack.append(val)

    def pop(self) -> None:
        
        self.stack.pop()
        if self.minorder[-1] == len(self.stack):
            self.minorder.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minorder[-1]]
