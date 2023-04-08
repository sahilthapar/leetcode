class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.cur_min))
        self.cur_min = min(self.cur_min, val) if self.cur_min is not None else val

    def pop(self) -> None:
        val, prev_min = self.stack.pop()
        self.cur_min = prev_min

    def top(self) -> int:
        val, prev_min = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.cur_min
