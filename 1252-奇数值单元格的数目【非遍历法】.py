class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r, c = dict(), dict()
        count_r, count_c = 0, 0
        lens = len(indices)
        for a in indices:
            if a[0] in r:
                r[a[0]] += 1
                if r[a[0]] % 2 == 0:
                    count_r -= 1
                else:
                    count_r += 1
            else:
                r[a[0]] = 1
                count_r += 1
            if a[1] in c:
                c[a[1]] += 1
                if c[a[1]] % 2 == 0:
                    count_c -= 1
                else:
                    count_c += 1
            else:
                c[a[1]] = 1
                count_c += 1
        print("count_r:", count_r, " count_c:", count_c)
        return count_r * n + count_c * m - 2 * count_r * count_c
