class Solution:
    def frequencySort(self, s: str) -> str:
        #count = dict()
        # for a in s:
        #     if a in count.keys():
        #         count[a] += 1
        #     else:
        #         count[a] = 1
        count = Counter(s) # 效率较高**
        # def dictSort(data) -> dict:
        #     return dict(sorted(data.items(), key = operator.itemgetter(1), reverse = True))
        #count = dictSort(count)
        count = OrderedDict(sorted(count.items(), key=lambda count:count[1], reverse=True))
        ans = ""
        for a in count.keys():
            #for i in range(count[a]):
            ans += a * count[a]
        return ans