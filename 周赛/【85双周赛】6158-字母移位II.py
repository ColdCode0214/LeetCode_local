class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(shifts)
        lens = len(s)
        arr = list()
        for i in range(lens):
            arr.append(ord(s[i]))
        # print(arr)
        count = dict()
        for i in range(n):
            if shifts[i][2] == 0:
                if shifts[i][0] in count:
                    count[shifts[i][0]] -= 1
                else:
                    count[shifts[i][0]] = -1
                if shifts[i][1] + 1 in count:
                    count[shifts[i][1] + 1] += 1
                else:
                    count[shifts[i][1] + 1] = 1
            else:
                if shifts[i][0] in count:
                    count[shifts[i][0]] += 1
                else:
                    count[shifts[i][0]] = 1
                if shifts[i][1] + 1 in count:
                    count[shifts[i][1] + 1] -= 1
                else:
                    count[shifts[i][1] + 1] = -1

        def sortDict(data) -> dict:
            return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=False))

        count = sortDict(count)
        # print("count:", count)
        cur = 0
        for i in range(lens):

            if i in count.keys():
                cur += count[i]
            arr[i] += cur
            if arr[i] > 122:
                diff = arr[i] - 122
                diff = diff % 26
                if diff == 0:
                    arr[i] = 122
                else:
                    arr[i] = diff + 96
            if arr[i] < 97:
                diff = 97 - arr[i]
                diff = diff % 26
                if diff == 0:
                    arr[i] = 97
                else:
                    arr[i] = 123 - diff
        # print("arr2:", arr)
        ans = ""
        for i in range(lens):
            ans += chr(arr[i])
        return ans


