#python默认的递归深度不够，需要手动设置
sys.setrecursionlimit(100000)
def f(n, m):
    if n == 0:
        return 0
    x = f(n-1, m)
    return (m+x)%n
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)