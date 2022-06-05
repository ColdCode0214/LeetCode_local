# 参考题解1：https://leetcode.cn/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/
# 参考题解2：https://leetcode.cn/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 通过哈希获取链表节点
        # 将该节点移至头部（表示最近使用过）
        # 返回节点的值
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 如果key不在cache中
        # 新增一个节点
        # 添加进哈希表中
        # 添加到链表头部
        # 如果超过容量
        # 删掉链表尾部元素
        # 删掉哈希表中对应项
        if key not in self.cache:
            node = DlinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1

        # 如果key在cache中
        # 通过哈希定位到链表节点
        # 更新链表节点的值
        # 将该节点移至链表头部
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):  # 此处需要注意更新的顺序
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)