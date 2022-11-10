class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        b = bin(n)
        # print("b:", b)
        sb = str(b)[2:]
        # print("sb:", sb)
        lens = len(sb)
        l = list()
        index = list()
        MOD = 1000000007
        for i in range(lens):
            if sb[i] == '1':
                # l.insert(0, pow(2, (lens-1-i)))
                index.insert(0, lens - 1 - i)
        # print("l:", l)
        lens2 = len(queries)
        ans = list()
        # m = [1]*(len(l)+1)
        # for i in range(1, len(l)+1):
        #     m[i] = (m[i-1]*l[i-1])

        # print("m:", m)
        # for i in range(lens2):
        #     ans.append(int(m[queries[i][1]+1] / m[queries[i][0]]))

        p = [0] * (len(index) + 1)
        for i in range(1, len(index) + 1):
            p[i] = p[i - 1] + index[i - 1]
        for i in range(lens2):
            cur = p[queries[i][1] + 1] - p[queries[i][0]]
            temp = 1
            for k in range(cur):
                temp *= 2
                temp %= MOD
            ans.append(temp)

        return ans