class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum = img[i][j]
                count = 1
                if i-1 > -1:
                    sum += img[i-1][j]
                    count += 1
                    if j-1 > -1:
                        sum += img[i-1][j-1]
                        count += 1
                    if j+1 < n:
                        sum += img[i-1][j+1]
                        count += 1
                if i+1 < m:
                    sum += img[i+1][j]
                    count += 1
                    if j-1 > -1:
                        sum += img[i+1][j-1]
                        count += 1
                    if j+1 < n:
                        sum += img[i+1][j+1]
                        count += 1
                if j-1 > -1:
                    sum += img[i][j-1]
                    count += 1
                if j+1 < n:
                    sum += img[i][j+1]
                    count += 1
                ans[i][j] = floor(sum/count)
        return ans


