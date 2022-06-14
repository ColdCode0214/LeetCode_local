class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        count = dict()
        for i in range(n):
            a = messages[i].split()
            if senders[i] not in count:
                count[senders[i]] = len(a)
            else:
                count[senders[i]] += len(a)
            # print(a)
            # print(senders[i], ":", count[senders[i]])
        count_max = 0
        ans = ""
        for k in count:
            if count[k] > count_max:
                ans = k
                count_max = count[k]
            elif count[k] == count_max and k > ans:
                ans = k
                count_max = count[k]
                # print("ans:", ans)
                # print("count:", count_max)
        # if "OXlq" > "FnZd":
        #     print("111")
        # else: print("222")
        return ans