class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        count2 = collections.Counter(count.values())
        # print(count)
        # print(count2)
        for a in count2.values():
            if a>1:
                return False
        return True