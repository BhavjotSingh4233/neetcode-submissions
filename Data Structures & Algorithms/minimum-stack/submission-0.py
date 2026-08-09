class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1: 
            self.min_val.append(val)
        else: 
            if val < self.min_val[-1]:
                self.min_val.append(val)
            else:
                self.min_val.append(self.min_val[-1])

        

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

        
