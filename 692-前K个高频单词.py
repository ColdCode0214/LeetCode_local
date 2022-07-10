class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        mp = dict()

        for i in words:
            if i in mp.keys():
                mp[i] += 1
            else:
                mp[i] = 1
        count = list()
        for a in mp.keys():
            count.append(mp[a])
        count.sort()
        count.reverse()
        print(count)
        ans = list()
        for i in range(k):
            for a in mp.keys():
                if mp[a] == count[i]:
                    ans.append(a)
                    mp[a] = 0
                    break
        return ans