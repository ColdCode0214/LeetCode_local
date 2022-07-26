class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        mp = dict()
        EnglishWord = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        for i in range(21):
            mp[i] = EnglishWord[i]
        mp[30], mp[40], mp[50], mp[60], mp[70], mp[80], mp[90] = 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'

        def toHundred(a, b, c) -> str:
            res = ''
            if a != 0:
                res = mp[a] + ' Hundred'
            if b == 0: #十位是0
                if c != 0: res += mp[c] #个位非0
            elif b == 1: #十位是1
                res += mp[b*10+c]
            else:      #十位非0
                b *= 10
                if c == 0: #个位是0
                    res += mp[b]
                else:
                    res += mp[b] + ' ' + mp[c]
            return res
        nums = list()

        for i in range(10):
            nums.append(num%10)
            num = int(num/10)
        nums.reverse()
        ans = ""

        if nums[0] != 0: ans += mp[nums[0]] +' Billion'
        for i in range(1,10,3):
            ans += toHundred(nums[i], nums[i+1], nums[i+2])
            if i == 1 and sum(nums[i:i+3]) != 0: ans += ' Million'
            elif i == 4 and sum(nums[i:i+3]) != 0: ans += ' Thousand'
        i = 0
        while i < len(ans):
            if i != 0 and (65<=ord(ans[i])<=90 and ans[i-1] != ' '):
                 ans = ans[0:i] + ' ' + ans[i:]
            i += 1
        return ans


