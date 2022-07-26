from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.i2n = dict()
        self.n2i = dict()


    def change(self, index: int, number: int) -> None:
        if index in self.i2n.keys():
            # 首先找到当前index原本存储的是什么数
            pre = self.i2n[index]
            # 移除pre数字的下标列表中的index
            self.n2i[pre].remove(index)
        # 更新index存储的数字
        self.i2n[index] = number
        # 更新number的下标列表
        if number not in self.n2i.keys():
            self.n2i[number] = SortedList()
        self.n2i[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.n2i.keys() or len(self.n2i[number]) == 0: return -1
        else:
            return self.n2i[number][0]



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)