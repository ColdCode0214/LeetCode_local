class Solution:
    def reverseWords(self, s: str) -> str:
        lens = len(s)
        str = ""
        temp = ""
        for i in range(lens):
            if s[i] == " ":
                if temp != "":
                    if str == "":
                        str = temp
                    else:
                        # str += temp
                        # str += " "
                        str = temp + " " + str
                    # str.insert(0,temp)
                    temp = ""
            else:
                temp += s[i]
                if i == lens - 1:
                    # str.insert(0,temp)
                    if str == "":
                        str = temp
                    else:
                        str = temp + " " + str
        return str

