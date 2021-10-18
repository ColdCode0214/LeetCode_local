class Solution:
    def reverseBits(self, num: int) -> int:
        cur, insert, res = 0, 0, 0
        for i in range(32):
            if num & (1 << i):
                cur+=1
                insert+=1
            else:
                insert=cur+1
                cur=0
            res=max(res, insert)
        return res