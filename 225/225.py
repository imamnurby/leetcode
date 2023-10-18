class MyStack:

    def __init__(self):
        self.stack = []
        self.idx_top = None
    
    def push(self, x: int) -> None:

        if self.stack:
            self.idx_top += 1
        else:
            self.idx_top = 0
        
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[self.idx_top]
        self.idx_top -= 1
        self.stack = self.stack[:self.idx_top+1]
        return x

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return False if self.stack else True
        
