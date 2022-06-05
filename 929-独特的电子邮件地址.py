class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        ans = 0
        plus_flag = 0
        at_flag = 0
        temp = ""
        emailList = list()
        for i in range(n):
            m = len(emails[i])
            temp = ""
            at_flag = 0
            plus_flag = 0
            for j in range(m):
                if emails[i][j] == "@":
                    at_flag = 1
                if at_flag == 1:
                    temp += emails[i][j]
                else:
                    if emails[i][j] == "+":
                        plus_flag = 1
                    if emails[i][j] != "." and plus_flag == 0:
                        temp += emails[i][j]
            if temp not in emailList:
                emailList.append(temp)
        #print(emailList)
        return len(emailList)