class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = dict()
        ans, temp = 0, ""
        for i in range(n):
            
            if s[i] in temp:
                ans = max(ans, len(temp))
                print("ttemp:", temp)
                print("mp[s[i]]:", mp[s[i]])
                temp = s[mp[s[i]]+1:i+1]
                print("temp0:", temp)
                mp[s[i]] = i
            else:
                temp += s[i]
                print("temp1:", temp)
                mp[s[i]] = i
        print("temp2:", temp)
        return max(ans, len(temp))