class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        # 为获得字典序上最小的字符串，需要把字母表中靠前的字母尽可能先移动到后面
        # 因为题目没有要求最小的移动次数，因此即使把最终排在首位的字母移动到后方也不影响，最终会被后面的字母顶回来
        # 挪过的字母增加标记
        # 终止条件？？？
        '''
        例如：baaca，k=3
        第一步：前三个字母为baa，字母表序列中最靠前的是a，因此将a挪到最后，得到bacaa
        第二步：前三个字母为bac，字母表序列中最靠前的是a，因此将a挪到最后，得到bcaaa
        第三步：前三个字母为bca，字母表序列中最靠前的是a，因此将a挪到最后，得到bcaaa
        第四步：前三个字母为bca，但a因为在第一步就挪过有过标记，不能再挪，因此挪动b，得到caaab
        第五步：前三个字母为caa，其中两个a均有标记，因此挪c，得到aaabc
        '''
        # 当k=1时按题意模拟，k>=2时一定可以升序排列
        if k == 1:
            ans = s
            for i in range(n):
                s = s[1:]+s[0]
                ans = min(ans, s)
            return ans
        else:
            return ''.join(sorted(s))

