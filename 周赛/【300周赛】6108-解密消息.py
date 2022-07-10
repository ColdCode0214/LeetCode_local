class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = dict()
        sta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        index = 0
        for a in key:
            if a != " ":
                if a not in mp.keys():
                    mp[a] = sta[index]
                    index += 1
        print(mp)
        ans = ""
        for a in message:
            if a != " ":
                ans += mp[a]
            else:
                ans += a
        return ans