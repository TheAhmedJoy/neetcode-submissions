class MyStack:

    def __init__(self):
        self.stack = None

    def push(self, x: int) -> None:
        self.stack = deque([x, self.stack])

    def pop(self) -> int:
        top = self.stack.popleft()
        self.stack = self.stack.popleft()
        return top

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()