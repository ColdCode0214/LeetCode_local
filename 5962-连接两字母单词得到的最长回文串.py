class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        same = collections.Counter()
        diff = collections.Counter()

        for word in words:
            if word[0] == word[1]:
                same[word] += 1
            else:
                diff[word] += 1

        ans = 0

        for word in diff:
            rev = word[::-1]
            if rev in diff:
                ans += min(diff[word], diff[rev]) * 2

        for word in same:
            ans += same[word] // 2 * 4
            same[word] %= 2

        for word in same:
            if same[word] == 1:
                ans += 2
                break

        return ans
