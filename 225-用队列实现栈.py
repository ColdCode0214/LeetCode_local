class MyStack:

    def __init__(self):
        self.a = list()


    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        temp = self.a.pop(len(self.a)-1)
        return temp

    def top(self) -> int:
        return self.a[len(self.a)-1]
        

    def empty(self) -> bool:
        if len(self.a) == 0: return True
        else: return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()