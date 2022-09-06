class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        arr = list()
        m, n = len(mat), len(mat[0])
        mp = dict()
        for i in range(m):
            flag = 0
            index = -1
            for j in range(n):
                if mat[i][j] == 1:
                    if flag == 0:
                        index = j
                        flag = 1
                    else:
                        flag = 2
                        break
            if flag == 1:
                if index in mp:
                    mp[index] += 1
                else:
                    mp[index] = 1
        for a in mp:
            if mp[a] == 1:
                arr.append(a)
        for j in arr:
            flag = 0
            for i in range(m):
                if mat[i][j] == 1:
                    if flag == 0:
                        flag = 1
                    else:
                        flag = 2
                        break
            if flag == 1:
                ans += 1
        return ans
